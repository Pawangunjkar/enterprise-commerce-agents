"""Journey: merchandising.

Domain journey / application *.
Catalog plus OMS affinity ranking.
"""

from ecs_agents.agents.spec import journey

SPEC = journey(
    slug='merchandising',
    title='Journey: merchandising',
    mission='Catalog plus OMS affinity ranking.',
    tools=('product-service.list_products', 'suite.recommend_skus', 'offer-promotion-service.create_offer'),
    keywords=('merchandising journey',),
    scenario='merchandising-upsell',
)
