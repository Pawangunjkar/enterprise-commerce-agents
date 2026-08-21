"""WMS pick wave.

Domain oms / application wms-fulfillment-service.
Release a warehouse pick wave.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='wms-fulfillment-service',
    slug='wms-wave',
    title='WMS pick wave',
    mission='Release a warehouse pick wave.',
    tools=('wms-fulfillment-service.create_wave',),
    keywords=('wms', 'pick wave', 'warehouse wave'),
)
