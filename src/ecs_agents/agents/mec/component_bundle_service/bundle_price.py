"""Bundle pricing.

Domain mec / application component-bundle-service.
Price a component bundle / kit.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='component-bundle-service',
    slug='bundle-price',
    title='Bundle pricing',
    mission='Price a component bundle / kit.',
    tools=('component-bundle-service.price_bundle',),
    keywords=('bundle', 'kit price'),
)
