"""Order admin NDR.

Domain portal / application order-admin-portal.
Ops NDR from order admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='order-admin-portal',
    slug='order-desk-ndr',
    title='Order admin NDR',
    mission='Ops NDR from order admin.',
    tools=('order-admin-portal.ndr_action',),
    keywords=('order admin ndr',),
)
