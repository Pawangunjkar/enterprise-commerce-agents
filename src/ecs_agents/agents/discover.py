"""Load AGENT (preferred) or SPEC from every operator module."""

from __future__ import annotations

import importlib
import pkgutil

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import AgentSpec

_SKIP = {"spec", "discover", "base", "tool_factory"}


def discover_bundle() -> dict[str, CommerceAgent]:
    import ecs_agents.agents as package

    bundle: dict[str, CommerceAgent] = {}
    for module_info in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        leaf = module_info.name.rsplit(".", 1)[-1]
        if leaf in _SKIP or module_info.ispkg:
            continue
        module = importlib.import_module(module_info.name)
        agent = getattr(module, "AGENT", None)
        if agent is None:
            spec = getattr(module, "SPEC", None)
            if spec is None:
                continue
            agent = CommerceAgent(spec=spec)
        if not isinstance(agent, CommerceAgent):
            continue
        spec = agent.spec
        bundle[spec.key] = agent
        if spec.kind == "journey":
            bundle[spec.slug] = agent
    return bundle


def specs_from(bundle: dict[str, CommerceAgent]) -> dict[str, AgentSpec]:
    return {key: agent.spec for key, agent in bundle.items()}
