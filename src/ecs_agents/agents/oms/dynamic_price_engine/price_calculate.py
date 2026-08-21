"""Dynamic price.

Domain oms / application dynamic-price-engine.
Calculate offer and loyalty adjusted INR price.
"""

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
