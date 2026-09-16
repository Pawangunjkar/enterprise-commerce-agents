"""Storefront UPI LangGraph agent.

Domain `portal` / application `ecommerce-storefront-portal`.
Buyer BharatQR from the storefront checkout.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='ecommerce-storefront-portal',
    slug='store-upi',
    title='Storefront UPI',
    mission='Buyer BharatQR from the storefront checkout.',
    tools=('ecommerce-storefront-portal.create_upi_qr',),
    keywords=('storefront upi', 'store qr'),
)


class StoreUpiAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `ecommerce-storefront-portal`. Buyer BharatQR from the storefront checkout. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = StoreUpiAgent()
