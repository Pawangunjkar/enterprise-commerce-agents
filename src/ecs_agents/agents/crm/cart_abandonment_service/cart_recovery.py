"""Cart abandonment LangGraph agent.

Domain `crm` / application `cart-abandonment-service`.
Mark a cart abandoned for recovery journeys.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='cart-abandonment-service',
    slug='cart-recovery',
    title='Cart abandonment',
    mission='Mark a cart abandoned for recovery journeys.',
    tools=('cart-abandonment-service.mark_abandoned',),
    keywords=('abandon', 'cart recovery'),
)


class CartRecoveryAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `cart-abandonment-service`. Mark a cart abandoned for recovery journeys. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CartRecoveryAgent()
