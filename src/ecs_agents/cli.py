from __future__ import annotations

import argparse
import asyncio
import os
from pathlib import Path

from ecs_agents.catalog import get_agent
from ecs_agents.graph import chat_once
from ecs_agents.mcp_hub import McpHub
from ecs_agents.registry import agents_by_domain, unique_agents
from ecs_agents.scenarios import list_scenario_ids, load_scenario, render_report, run_scenario
from ecs_agents.settings import load_settings


def _load_dotenv() -> None:
    path = Path(".env")
    if not path.is_file():
        path = Path(__file__).resolve().parents[2] / ".env"
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, _, value = stripped.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


async def _run_named(scenario_id: str) -> int:
    settings = load_settings()
    async with McpHub(settings) as hub:
        result = await run_scenario(hub, scenario_id)
    print(render_report(result))
    return 0 if result.get("ok") else 1


async def _chat(text: str) -> int:
    settings = load_settings()
    async with McpHub(settings) as hub:
        print(await chat_once(settings, hub, text))
    return 0


def _print_agents(domain: str, application: str) -> None:
    specs = unique_agents()
    if domain:
        specs = [s for s in specs if s.domain == domain]
    if application:
        specs = [s for s in specs if s.application == application]
        print(f"{len(specs)} agents  (domain={domain or '*'} application={application or '*'})")
    tree = agents_by_domain()
    for domain_name, apps in tree.items():
        if domain and domain_name != domain:
            continue
        header = False
        for app_name, agents in apps.items():
            if application and app_name != application:
                continue
            if not header:
                print(f"\n## {domain_name}")
                header = True
            print(f"  {app_name}  ({len(agents)})")
            for spec in agents:
                extra = f"  playbook={spec.default_scenario}" if spec.default_scenario else ""
                print(f"    - {spec.slug:24} {type(get_agent(spec.key)).__name__:28} {spec.title}{extra}")


def main() -> None:
    _load_dotenv()
    parser = argparse.ArgumentParser(
        description="LangGraph + MCP business agents for Enterprise Commerce Suite (not FAQ bots)."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    list_p = sub.add_parser("list-agents", help="Show domain / application / specialist agents")
    list_p.add_argument("--domain", default="", help="platform|mec|oms|billing|crm|portal|journey")
    list_p.add_argument("--application", default="", help="MCP server / Spring app name")

    sub.add_parser("list-scenarios", help="Show live business playbooks")

    run_p = sub.add_parser("run", help="Execute a named scenario against live MCP tools")
    run_p.add_argument("scenario")

    chat_p = sub.add_parser("chat", help="LangGraph ReAct chat (OpenAI or Gemini key) or heuristic route")
    chat_p.add_argument("text", nargs="+")

    serve_p = sub.add_parser("serve", help="HTTP API for chat and scenarios")
    serve_p.add_argument("--host", default="127.0.0.1")
    serve_p.add_argument("--port", type=int, default=8099)

    args = parser.parse_args()
    if args.cmd == "list-agents":
        _print_agents(args.domain, args.application)
        return
    if args.cmd == "list-scenarios":
        for scenario_id in list_scenario_ids():
            spec = load_scenario(scenario_id)
            print(f"{scenario_id:28} [{spec.get('agent')}] {spec.get('title')}")
        return
    if args.cmd == "run":
        raise SystemExit(asyncio.run(_run_named(args.scenario)))
    if args.cmd == "chat":
        raise SystemExit(asyncio.run(_chat(" ".join(args.text))))
    if args.cmd == "serve":
        import uvicorn

        from ecs_agents.serve import app

        uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
