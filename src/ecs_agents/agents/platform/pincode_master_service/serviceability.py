"""Serviceability and EDD.

Domain platform / application pincode-master-service.
Origin vs destination serviceability, ODA, EDD.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='pincode-master-service',
    slug='serviceability',
    title='Serviceability and EDD',
    mission='Origin vs destination serviceability, ODA, EDD.',
    tools=('pincode-master-service.serviceability',),
    keywords=('serviceability', 'edd', 'oda'),
)
