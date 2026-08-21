"""OMS catalog consumer.

Domain oms / application catalog-consumer-service.
OMS replica consumer health probe.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='catalog-consumer-service',
    slug='oms-catalog-consumer',
    title='OMS catalog consumer',
    mission='OMS replica consumer health probe.',
    tools=('catalog-consumer-service.health',),
    keywords=('catalog consumer', 'oms replica'),
)
