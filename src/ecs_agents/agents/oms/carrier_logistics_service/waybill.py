"""Waybill create.

Domain oms / application carrier-logistics-service.
Create a carrier waybill/AWB.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='carrier-logistics-service',
    slug='waybill',
    title='Waybill create',
    mission='Create a carrier waybill/AWB.',
    tools=('carrier-logistics-service.create_waybill',),
    keywords=('waybill', 'awb create', 'shipment'),
)
