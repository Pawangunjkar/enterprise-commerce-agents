"""Agent catalog assembled by discovering per-agent modules."""

from __future__ import annotations

from ecs_agents.agents.discover import discover_agents
from ecs_agents.agents.spec import APPLICATIONS, AgentSpec, DOMAINS

AGENTS: dict[str, AgentSpec] = discover_agents()


def unique_agents() -> list[AgentSpec]:
    seen: set[str] = set()
    ordered: list[AgentSpec] = []
    for spec in AGENTS.values():
        if spec.key in seen:
            continue
        seen.add(spec.key)
        ordered.append(spec)
    return ordered
