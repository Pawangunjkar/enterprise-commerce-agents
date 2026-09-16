"""Variant matrix LangGraph agent.

Domain `mec` / application `variant-matrix-service`.
Explode RAM/color/storage variant combinations.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='variant-matrix-service',
    slug='variant-explode',
    title='Variant matrix',
    mission='Explode RAM/color/storage variant combinations.',
    tools=('variant-matrix-service.explode_variants',),
    keywords=('variant', 'variant matrix', 'explode'),
)


class VariantExplodeAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `variant-matrix-service`. Explode RAM/color/storage variant combinations. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = VariantExplodeAgent()
