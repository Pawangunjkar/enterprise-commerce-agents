"""EMI quote LangGraph agent.

Domain `billing` / application `subscription-emi-service`.
Quote subscription/EMI on principal and tenure.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='subscription-emi-service',
    slug='emi-quote',
    title='EMI quote',
    mission='Quote subscription/EMI on principal and tenure.',
    tools=('subscription-emi-service.emi_quote',),
    keywords=('emi', 'no cost emi', 'tenure'),
)


class EmiQuoteAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `subscription-emi-service`. Quote subscription/EMI on principal and tenure. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = EmiQuoteAgent()
