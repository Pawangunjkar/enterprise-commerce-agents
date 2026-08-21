"""DPDP consent.

Domain crm / application dpdp-compliance-service.
Record DPDP Act 2023 consent.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='dpdp-compliance-service',
    slug='dpdp-consent',
    title='DPDP consent',
    mission='Record DPDP Act 2023 consent.',
    tools=('dpdp-compliance-service.record_consent',),
    keywords=('dpdp', 'consent', 'dpdp act'),
)
