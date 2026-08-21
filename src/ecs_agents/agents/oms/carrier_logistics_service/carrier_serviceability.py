"""Carrier serviceability.

Domain oms / application carrier-logistics-service.
Ask Delhivery/Shiprocket/BlueDart style serviceability.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='carrier-logistics-service',
    slug='carrier-serviceability',
    title='Carrier serviceability',
    mission='Ask Delhivery/Shiprocket/BlueDart style serviceability.',
    tools=('carrier-logistics-service.check_serviceability',),
    keywords=('carrier serviceability', 'delhivery', 'shiprocket'),
)
