"""LangGraph operator agents: each module exports AGENT, not just a SPEC dict."""

from __future__ import annotations

from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent

from ecs_agents.agents.spec import AgentSpec
from ecs_agents.agents.tool_factory import mcp_tools
from ecs_agents.mcp_hub import McpHub

SHARED_RULES = """You are a live Enterprise Commerce Suite operator, not a FAQ or help-center bot.
You MUST call your bound MCP tools for any fact (price, GST, stock, order id, QR, OTP).
Never invent INR amounts, tax types, AWBs, invoice numbers, or IMEIs.
If a tool returns {"error": ...} or an HTTP failure, quote that payload.
Indian commerce: INR, HSN, GST (CGST+SGST vs IGST), UPI/BharatQR, pincode EDD, DPDP 2023.
Keep the final answer short and cite tool JSON (ids, taxType, remaining stock).
"""


class CommerceAgent:
    """One LangGraph ReAct agent bound to a suite application (or a journey of apps)."""

    spec: AgentSpec
    instructions: str = ""

    def __init__(self, spec: AgentSpec | None = None, instructions: str = "") -> None:
        if spec is not None:
            self.spec = spec
        if instructions:
            self.instructions = instructions
        if not getattr(self, "spec", None):
            raise TypeError(f"{type(self).__name__} needs spec")

    @property
    def key(self) -> str:
        return self.spec.key

    @property
    def system_prompt(self) -> str:
        extra = self.instructions.strip() or self.spec.mission
        tools = ", ".join(self.spec.tools)
        return (
            f"{SHARED_RULES}\n"
            f"Agent key: {self.spec.key}\n"
            f"Domain: {self.spec.domain} | Application: {self.spec.application}\n"
            f"Role: {self.spec.title}\n"
            f"{extra}\n"
            f"Bound MCP tools: {tools}\n"
            f"Call tools with named JSON fields, never empty guesses when the user supplied values."
        )

    def bind_tools(self, hub: McpHub):
        return mcp_tools(hub, list(self.spec.tools))

    def compile(self, llm: BaseChatModel, hub: McpHub):
        return create_react_agent(
            llm,
            tools=self.bind_tools(hub),
            prompt=self.system_prompt,
            name=self.spec.slug.replace("-", "_")[:64],
        )

    async def ainvoke(self, llm: BaseChatModel, hub: McpHub, user_text: str) -> str:
        await hub.start(self.spec.servers)
        graph = self.compile(llm, hub)
        result = await graph.ainvoke(
            {"messages": [SystemMessage(content=self.system_prompt), HumanMessage(content=user_text)]}
        )
        last = result["messages"][-1]
        content = getattr(last, "content", last)
        return content if isinstance(content, str) else str(content)

    def as_dict(self) -> dict[str, Any]:
        return {
            "key": self.spec.key,
            "class": type(self).__name__,
            "domain": self.spec.domain,
            "application": self.spec.application,
            "slug": self.spec.slug,
            "title": self.spec.title,
            "kind": self.spec.kind,
            "tools": list(self.spec.tools),
            "mcpServers": list(self.spec.servers),
            "defaultScenario": self.spec.default_scenario or None,
        }
