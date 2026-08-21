"""B2B tier quote.

Domain mec / application b2b-tiered-catalog-service.
Quote a dealer/distributor tier price.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='b2b-tiered-catalog-service',
    slug='b2b-quote',
    title='B2B tier quote',
    mission='Quote a dealer/distributor tier price.',
    tools=('b2b-tiered-catalog-service.b2b_quote',),
    keywords=('b2b', 'dealer price', 'tier quote'),
)
