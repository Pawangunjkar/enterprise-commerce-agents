"""Stdio MCP hub: launches enterprise-commerce-mcps FastMCP servers and calls their tools."""

from __future__ import annotations

import json
import os
import sys
from contextlib import AsyncExitStack
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent

from ecs_agents.agents.spec import mcp_module
from ecs_agents.settings import Settings
from ecs_agents.suite_http import SuiteHttp, extra_tool_specs, invoke_extra


def _tool_payload(result: Any) -> Any:
    if getattr(result, "structuredContent", None):
        return result.structuredContent
    texts: list[str] = []
    for block in getattr(result, "content", []) or []:
        if isinstance(block, TextContent):
            texts.append(block.text)
        elif getattr(block, "text", None):
            texts.append(block.text)
    if not texts:
        return {"ok": True}
    raw = texts[0]
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"text": raw}


class McpHub:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.http = SuiteHttp(settings)
        self._stack = AsyncExitStack()
        self._sessions: dict[str, ClientSession] = {}

    async def __aenter__(self) -> McpHub:
        await self._stack.__aenter__()
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self._stack.__aexit__(*exc)
        self._sessions.clear()

    async def start(self, servers: list[str] | tuple[str, ...]) -> None:
        python = self.settings.mcp_python or sys.executable
        env = os.environ.copy()
        env["ECS_GATEWAY_URL"] = self.settings.gateway_url
        env["ECS_SERVICE_URL"] = self.settings.gateway_url
        env["ECS_TENANT_ID"] = self.settings.tenant_id
        if self.settings.bearer_token:
            env["ECS_BEARER_TOKEN"] = self.settings.bearer_token
        env["PYTHONUNBUFFERED"] = "1"
        for server in servers:
            if server in self._sessions:
                continue
            params = StdioServerParameters(
                command=python,
                args=["-m", mcp_module(server)],
                env=env,
            )
            read, write = await self._stack.enter_async_context(stdio_client(params))
            session = await self._stack.enter_async_context(ClientSession(read, write))
            await session.initialize()
            self._sessions[server] = session

    async def call(self, qualified: str, arguments: dict[str, Any] | None = None) -> Any:
        arguments = arguments or {}
        if qualified.startswith("suite."):
            return invoke_extra(self.http, qualified, arguments)
        if "." not in qualified:
            raise ValueError(f"Tool must be server.tool, got {qualified}")
        server, name = qualified.split(".", 1)
        if server not in self._sessions:
            await self.start([server])
        session = self._sessions[server]
        result = await session.call_tool(name, arguments)
        return _tool_payload(result)

    async def list_tools(self) -> list[dict[str, str]]:
        listed: list[dict[str, str]] = []
        for server, session in self._sessions.items():
            catalog = await session.list_tools()
            for tool in catalog.tools:
                listed.append(
                    {
                        "qualified": f"{server}.{tool.name}",
                        "description": tool.description or "",
                    }
                )
        for extra in extra_tool_specs():
            listed.append({"qualified": extra["name"], "description": extra["description"]})
        return listed
