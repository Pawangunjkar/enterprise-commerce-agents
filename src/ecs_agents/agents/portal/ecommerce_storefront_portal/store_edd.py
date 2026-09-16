"""Storefront EDD LangGraph agent.

Domain `portal` / application `ecommerce-storefront-portal`.
Buyer EDD check from the storefront.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='ecommerce-storefront-portal',
    slug='store-edd',
    title='Storefront EDD',
    mission='Buyer EDD check from the storefront.',
    tools=('ecommerce-storefront-portal.check_edd',),
    keywords=('storefront edd', 'check edd'),
)


class StoreEddAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `ecommerce-storefront-portal`. Buyer EDD check from the storefront. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = StoreEddAgent()
