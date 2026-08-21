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


def build_graph(llm: BaseChatModel, hub: McpHub, agent_key: str):
    spec = AGENTS[agent_key]
    tools = langchain_tools(hub, list(spec.tools))
    specialist = create_react_agent(llm, tools, prompt=prompt_for(agent_key))

    async def route(state: AgentState) -> dict[str, str]:
        last = ""
        for message in reversed(state["messages"]):
            if isinstance(message, HumanMessage) or getattr(message, "type", "") == "human":
                last = message.content if isinstance(message.content, str) else str(message.content)
                break
        return {"agent": route_agent(last)}

    async def run_specialist(state: AgentState) -> dict[str, Any]:
        key = state.get("agent") or agent_key
        if key != spec.key and key in AGENTS:
            other = AGENTS[key]
            graph = create_react_agent(llm, langchain_tools(hub, list(other.tools)), prompt=prompt_for(key))
            result = await graph.ainvoke({"messages": state["messages"]})
            return {"messages": result["messages"]}
        result = await specialist.ainvoke({"messages": state["messages"]})
        return {"messages": result["messages"]}

    graph = StateGraph(AgentState)
    graph.add_node("route", route)
    graph.add_node("specialist", run_specialist)
    graph.add_edge(START, "route")
    graph.add_edge("route", "specialist")
    graph.add_edge("specialist", END)
    return graph.compile()


async def chat_once(settings: Settings, hub: McpHub, text: str) -> str:
    key = route_agent(text)
    spec = AGENTS[key]
    llm = load_llm(settings)
    if llm is None:
        hint = spec.default_scenario or spec.key
        return (
            f"No OPENAI_API_KEY set. Routed to **{spec.title}** (`{spec.key}`)\n"
            f"domain={spec.domain} application={spec.application} kind={spec.kind}\n"
            f"MCP: {', '.join(spec.servers) or 'suite extras'}\n"
            f"Run a live playbook if listed: ecs-agents run {hint}"
        )
    await hub.start(spec.servers)
    graph = build_graph(llm, hub, spec.key)
    result = await graph.ainvoke(
        {
            "messages": [SystemMessage(content=prompt_for(spec.key)), HumanMessage(content=text)],
            "agent": spec.key,
        }
    )
    last = result["messages"][-1]
    content = getattr(last, "content", last)
    return content if isinstance(content, str) else str(content)
