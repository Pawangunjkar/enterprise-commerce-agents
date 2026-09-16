"""Catalog studio time-travel LangGraph agent.

Domain `portal` / application `catalog-admin-studio`.
As-of catalog from catalog studio.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='catalog-admin-studio',
    slug='studio-temporal',
    title='Catalog studio time-travel',
    mission='As-of catalog from catalog studio.',
    tools=('catalog-admin-studio.time_travel',),
    keywords=('studio time travel',),
)


class StudioTemporalAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `catalog-admin-studio`. As-of catalog from catalog studio. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = StudioTemporalAgent()
