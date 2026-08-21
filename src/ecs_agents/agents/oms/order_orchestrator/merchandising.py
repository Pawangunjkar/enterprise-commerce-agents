"""OMS merchandising.

Domain oms / application order-orchestrator.
Cross-sell and up-sell from affinity rules and SKU ladder.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='order-orchestrator',
    slug='merchandising',
    title='OMS merchandising',
    mission='Cross-sell and up-sell from affinity rules and SKU ladder.',
    tools=('suite.recommend_skus',),
    keywords=('cross-sell', 'upsell', 'up-sell', 'recommend', 'affinity'),
    scenario='merchandising-upsell',
)
