"""Order admin wave.

Domain portal / application order-admin-portal.
Ops WMS wave from order admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='order-admin-portal',
    slug='order-desk-wave',
    title='Order admin wave',
    mission='Ops WMS wave from order admin.',
    tools=('order-admin-portal.create_wave',),
    keywords=('order admin wave',),
)
