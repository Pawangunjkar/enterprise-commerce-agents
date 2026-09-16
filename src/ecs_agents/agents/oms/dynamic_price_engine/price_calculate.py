"""Dynamic price LangGraph agent.

Domain `oms` / application `dynamic-price-engine`.
Calculate offer and loyalty adjusted INR price.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='dynamic-price-engine',
    slug='price-calculate',
    title='Dynamic price',
    mission='Calculate offer and loyalty adjusted INR price.',
    tools=('dynamic-price-engine.calculate_price',),
    keywords=('dynamic price', 'calculate price'),
)


class PriceCalculateAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `dynamic-price-engine`. Calculate offer and loyalty adjusted INR price. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = PriceCalculateAgent()
