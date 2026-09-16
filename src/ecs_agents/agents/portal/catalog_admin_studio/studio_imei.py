"""Catalog studio IMEI LangGraph agent.

Domain `portal` / application `catalog-admin-studio`.
IMEI ingest from catalog studio.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='catalog-admin-studio',
    slug='studio-imei',
    title='Catalog studio IMEI',
    mission='IMEI ingest from catalog studio.',
    tools=('catalog-admin-studio.ingest_imei',),
    keywords=('studio imei',),
)


class StudioImeiAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `catalog-admin-studio`. IMEI ingest from catalog studio. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = StudioImeiAgent()
