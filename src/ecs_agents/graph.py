from __future__ import annotations

from typing import Annotated, Any, TypedDict

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import create_react_agent

from ecs_agents.lc_tools import langchain_tools
from ecs_agents.mcp_hub import McpHub
from ecs_agents.prompts import prompt_for
from ecs_agents.registry import AGENTS, route_agent
from ecs_agents.settings import Settings

# Tools the ReAct agent is allowed to call, by role (server.tool).
AGENT_TOOLS: dict[str, list[str]] = {
    "checkout": [
        "pincode-master-service.serviceability",
        "pincode-master-service.get_pincode",
        "product-service.list_products",
        "cart-service.add_cart_item",
        "atp-inventory-service.lock_stock",
        "gst-tax-engine.compute_gst",
        "order-orchestrator.place_order",
        "payment-gateway-service.create_bharat_qr",
        "suite.recommend_skus",
        "suite.get_order",
    ],
    "tax": [
        "gst-tax-engine.compute_gst",
        "gst-tax-engine.eway_bill",
        "tcs-tds-compliance-engine.compute_tcs_194o",
    ],
    "merchandising": [
        "product-service.list_products",
        "suite.recommend_skus",
        "offer-promotion-service.create_offer",
    ],
    "fulfillment": [
        "atp-inventory-service.lock_stock",
        "wms-fulfillment-service.create_wave",
        "ndr-returns-rma-service.ndr_action",
    ],
    "billing": [
        "payment-gateway-service.create_bharat_qr",
        "payment-gateway-service.payment_status",
        "invoice-service.issue_invoice",
        "dunning-service.dunning_schedule",
        "gst-tax-engine.compute_gst",
    ],
    "crm": [
        "customer-360-service.otp_start",
        "customer-360-service.otp_verify",
        "customer-360-service.upsert_profile",
        "support-ticket-service.create_ticket",
        "loyalty-rewards-service.get_loyalty",
        "cart-abandonment-service.mark_abandoned",
        "dpdp-compliance-service.record_consent",
    ],
}


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    agent: str


def load_llm(settings: Settings) -> BaseChatModel | None:
    if not settings.openai_api_key:
        return None
    kwargs: dict[str, Any] = {
        "model": settings.openai_model,
        "api_key": settings.openai_api_key,
        "temperature": 0,
    }
    if settings.openai_base_url:
        kwargs["base_url"] = settings.openai_base_url
    return ChatOpenAI(**kwargs)


def build_graph(llm: BaseChatModel, hub: McpHub):
    specialists = {}
    for key, names in AGENT_TOOLS.items():
        tools = langchain_tools(hub, names)
        specialists[key] = create_react_agent(llm, tools, prompt=prompt_for(key))

    async def route(state: AgentState) -> dict[str, str]:
        last = ""
        for message in reversed(state["messages"]):
            if isinstance(message, HumanMessage) or getattr(message, "type", "") == "human":
                last = message.content if isinstance(message.content, str) else str(message.content)
                break
        return {"agent": route_agent(last)}

    async def run_specialist(state: AgentState) -> dict[str, Any]:
        key = state["agent"]
        result = await specialists[key].ainvoke({"messages": state["messages"]})
        return {"messages": result["messages"]}

    graph = StateGraph(AgentState)
    graph.add_node("route", route)
    graph.add_node("specialist", run_specialist)
    graph.add_edge(START, "route")
    graph.add_edge("route", "specialist")
    graph.add_edge("specialist", END)
    return graph.compile()


async def chat_once(settings: Settings, hub: McpHub, text: str) -> str:
    llm = load_llm(settings)
    if llm is None:
        key = route_agent(text)
        spec = AGENTS[key]
        return (
            f"No OPENAI_API_KEY set. Heuristic route → **{spec.title}** (`{key}`).\n"
            f"This project is not an FAQ bot. Run a live scenario:\n"
            f"  ecs-agents run {spec.default_scenario}\n"
            f"Or set OPENAI_API_KEY and retry chat so the LangGraph ReAct agent can call MCP tools."
        )
    key = route_agent(text)
    await hub.start(AGENTS[key].servers)
    graph = build_graph(llm, hub)
    result = await graph.ainvoke(
        {
            "messages": [SystemMessage(content=prompt_for(key)), HumanMessage(content=text)],
            "agent": key,
        }
    )
    last = result["messages"][-1]
    content = getattr(last, "content", last)
    return content if isinstance(content, str) else str(content)
