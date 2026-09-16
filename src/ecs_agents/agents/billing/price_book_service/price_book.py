"""Price book LangGraph agent.

Domain `billing` / application `price-book-service`.
Read contractual price-book for a SKU.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='price-book-service',
    slug='price-book',
    title='Price book',
    mission='Read contractual price-book for a SKU.',
    tools=('price-book-service.get_price_book',),
    keywords=('price book', 'contract price'),
)


class PriceBookAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `price-book-service`. Read contractual price-book for a SKU. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = PriceBookAgent()
