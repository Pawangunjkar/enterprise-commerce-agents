"""Public agent registry: domain / application / specialist (+ journey aliases)."""

from __future__ import annotations

from collections import defaultdict

from ecs_agents.agents.spec import APPLICATIONS, AgentSpec, mcp_module
from ecs_agents.catalog import AGENTS, unique_agents

__all__ = [
    "AGENTS",
    "APPLICATIONS",
    "AgentSpec",
    "agents_by_domain",
    "mcp_module",
    "route_agent",
    "unique_agents",
]


def agents_by_domain() -> dict[str, dict[str, list[AgentSpec]]]:
    tree: dict[str, dict[str, list[AgentSpec]]] = defaultdict(lambda: defaultdict(list))
    for spec in unique_agents():
        tree[spec.domain][spec.application].append(spec)
    return {domain: dict(apps) for domain, apps in tree.items()}


def route_agent(text: str) -> str:
    blob = text.lower()
    scored: list[tuple[int, int, str]] = []
    for spec in unique_agents():
        hits = sum(1 for word in spec.keywords if word and word in blob)
        specialist_boost = 0 if spec.kind == "specialist" else 1
        scored.append((hits, specialist_boost, spec.key))
    scored.sort(key=lambda item: (-item[0], item[1], item[2]))
    if scored[0][0] == 0:
        return "oms.order-orchestrator.checkout-saga"
    return scored[0][2]
