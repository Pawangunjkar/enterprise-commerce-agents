"""Loyalty balance LangGraph agent.

Domain `crm` / application `loyalty-rewards-service`.
Read loyalty points with festival multiplier.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='loyalty-rewards-service',
    slug='loyalty-balance',
    title='Loyalty balance',
    mission='Read loyalty points with festival multiplier.',
    tools=('loyalty-rewards-service.get_loyalty',),
    keywords=('loyalty', 'reward points', 'festival multiplier'),
)


class LoyaltyBalanceAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `loyalty-rewards-service`. Read loyalty points with festival multiplier. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = LoyaltyBalanceAgent()
