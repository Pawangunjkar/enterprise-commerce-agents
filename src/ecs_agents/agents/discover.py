"""Load SPEC from every agent module under ecs_agents.agents."""

from __future__ import annotations

import importlib
import pkgutil
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ecs_agents.agents.spec import AgentSpec


def discover_agents() -> dict[str, "AgentSpec"]:
    import ecs_agents.agents as package

    catalog: dict[str, AgentSpec] = {}
    for module_info in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        if module_info.name.endswith(".spec") or module_info.name.endswith(".discover"):
            continue
        module = importlib.import_module(module_info.name)
        spec = getattr(module, "SPEC", None)
        if spec is None:
            continue
        catalog[spec.key] = spec
        if spec.kind == "journey":
            catalog[spec.slug] = spec
    return catalog
