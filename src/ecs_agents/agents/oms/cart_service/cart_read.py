"""Cart read.

Domain oms / application cart-service.
Load a cart by id from cart-service.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='cart-service',
    slug='cart-read',
    title='Cart read',
    mission='Load a cart by id from cart-service.',
    tools=('cart-service.get_cart',),
    keywords=('get cart', 'view cart'),
)
