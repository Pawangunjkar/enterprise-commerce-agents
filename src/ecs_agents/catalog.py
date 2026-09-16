"""Agent catalog assembled by discovering per-agent modules."""

from __future__ import annotations

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.discover import discover_bundle, specs_from
from ecs_agents.agents.spec import APPLICATIONS, AgentSpec, DOMAINS

BUNDLE: dict[str, CommerceAgent] = discover_bundle()
AGENTS: dict[str, AgentSpec] = specs_from(BUNDLE)


def get_agent(key: str) -> CommerceAgent:
    if key not in BUNDLE:
        raise KeyError(f"Unknown agent {key}")
    return BUNDLE[key]


def unique_agents() -> list[AgentSpec]:
    seen: set[str] = set()
    ordered: list[AgentSpec] = []
    for spec in AGENTS.values():
        if spec.key in seen:
            continue
        seen.add(spec.key)
        ordered.append(spec)
    return ordered
