"""Journey: merchandising LangGraph agent.

Domain `journey` / application `*`.
Catalog plus OMS affinity ranking.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import journey

SPEC = journey(
    slug='merchandising',
    title='Journey: merchandising',
    mission='Catalog plus OMS affinity ranking.',
    tools=('product-service.list_products', 'suite.recommend_skus', 'offer-promotion-service.create_offer'),
    keywords=('merchandising journey',),
    scenario='merchandising-upsell',
)


class MerchandisingAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You own this cross-application journey. Call MCP tools in business order when the user wants the full flow: product-service.list_products -> suite.recommend_skus -> offer-promotion-service.create_offer. Stop and report if any step errors. Catalog plus OMS affinity ranking.'


AGENT = MerchandisingAgent()
