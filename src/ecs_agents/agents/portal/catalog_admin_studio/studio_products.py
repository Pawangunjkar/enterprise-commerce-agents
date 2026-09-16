"""Catalog studio products LangGraph agent.

Domain `portal` / application `catalog-admin-studio`.
Merchandiser product list in catalog studio.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='catalog-admin-studio',
    slug='studio-products',
    title='Catalog studio products',
    mission='Merchandiser product list in catalog studio.',
    tools=('catalog-admin-studio.list_products',),
    keywords=('catalog studio', 'studio products'),
)


class StudioProductsAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `catalog-admin-studio`. Merchandiser product list in catalog studio. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = StudioProductsAgent()
