from __future__ import annotations

from langchain_core.tools import StructuredTool

from ecs_agents.mcp_hub import McpHub
from ecs_agents.suite_http import dump
import json


def langchain_tools(hub: McpHub, qualified_names: list[str]) -> list[StructuredTool]:
    tools: list[StructuredTool] = []
    for qualified in qualified_names:
        tools.append(_make_tool(hub, qualified))
    return tools


def _make_tool(hub: McpHub, qualified: str) -> StructuredTool:
    async def _run(arguments_json: str = "{}") -> str:
        try:
            parsed = json.loads(arguments_json or "{}")
        except json.JSONDecodeError:
            parsed = {}
        if not isinstance(parsed, dict):
            parsed = {"value": parsed}
        payload = await hub.call(qualified, parsed)
        return dump(payload)

    safe = qualified.replace(".", "__").replace("-", "_")
    return StructuredTool.from_function(
        coroutine=_run,
        name=safe[:64],
        description=f"Live Enterprise Commerce MCP tool `{qualified}`. Pass JSON object as arguments_json. Returns suite JSON, never invented FAQs.",
    )
