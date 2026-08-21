from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from ecs_agents.mcp_hub import McpHub
from ecs_agents.registry import AGENTS


def scenarios_dir() -> Path:
    env = Path(__file__).resolve().parents[2] / "scenarios"
    return env


def load_scenario(scenario_id: str) -> dict[str, Any]:
    path = scenarios_dir() / f"{scenario_id}.yaml"
    if not path.is_file():
        raise FileNotFoundError(f"Unknown scenario '{scenario_id}'. Available: {list_scenario_ids()}")
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def list_scenario_ids() -> list[str]:
    folder = scenarios_dir()
    if not folder.is_dir():
        return []
    return sorted(p.stem for p in folder.glob("*.yaml"))


def resolve_value(value: Any, ctx: dict[str, Any]) -> Any:
    if isinstance(value, str) and value.startswith("$."):
        return _dig(ctx, value[2:])
    if isinstance(value, list):
        return [resolve_value(item, ctx) for item in value]
    if isinstance(value, dict):
        return {key: resolve_value(item, ctx) for key, item in value.items()}
    return value


def _dig(ctx: dict[str, Any], path: str) -> Any:
    current: Any = ctx
    for part in path.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
            continue
        if isinstance(current, dict) and "data" in current and isinstance(current["data"], dict) and part in current["data"]:
            current = current["data"][part]
            continue
        if isinstance(current, list) and part.isdigit():
            current = current[int(part)]
            continue
        raise KeyError(f"Cannot resolve $.{path} at '{part}'")
    return current


async def run_scenario(hub: McpHub, scenario_id: str) -> dict[str, Any]:
    spec = load_scenario(scenario_id)
    agent_key = spec["agent"]
    await hub.start(AGENTS[agent_key].servers)
    ctx: dict[str, Any] = {}
    steps_out: list[dict[str, Any]] = []
    for index, step in enumerate(spec.get("steps") or [], start=1):
        qualified = step["call"]
        arguments = resolve_value(step.get("args") or {}, ctx)
        result = await hub.call(qualified, arguments)
        step_id = step.get("id") or f"step{index}"
        ctx[step_id] = result
        ctx["last"] = result
        record = {
            "id": step_id,
            "call": qualified,
            "args": arguments,
            "result": result,
        }
        steps_out.append(record)
        if isinstance(result, dict) and result.get("error"):
            return {
                "scenario": scenario_id,
                "ok": False,
                "failed_step": step_id,
                "steps": steps_out,
            }
    return {
        "scenario": scenario_id,
        "ok": True,
        "title": spec.get("title"),
        "business": spec.get("business"),
        "steps": steps_out,
    }


def render_report(run: dict[str, Any]) -> str:
    lines = [
        f"# {run.get('title') or run['scenario']}",
        f"ok={run.get('ok')}  scenario={run['scenario']}",
        run.get("business") or "",
        "",
    ]
    for step in run.get("steps") or []:
        lines.append(f"## {step['id']}: {step['call']}")
        lines.append("```json")
        lines.append(json.dumps(step["result"], indent=2, default=str)[:4000])
        lines.append("```")
        lines.append("")
    return "\n".join(lines)
