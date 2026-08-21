"""Cart mutate.

Domain oms / application cart-service.
Add line items to a live cart.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='cart-service',
    slug='cart-mutate',
    title='Cart mutate',
    mission='Add line items to a live cart.',
    tools=('cart-service.add_cart_item',),
    keywords=('add to cart', 'cart item'),
)
