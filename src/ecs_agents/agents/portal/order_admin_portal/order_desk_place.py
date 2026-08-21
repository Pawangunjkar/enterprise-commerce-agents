"""Order admin place.

Domain portal / application order-admin-portal.
Ops place-order from order admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='order-admin-portal',
    slug='order-desk-place',
    title='Order admin place',
    mission='Ops place-order from order admin.',
    tools=('order-admin-portal.place_order',),
    keywords=('order admin', 'ops place order'),
)
