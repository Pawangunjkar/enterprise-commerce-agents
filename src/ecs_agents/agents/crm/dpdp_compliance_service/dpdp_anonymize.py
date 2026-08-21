"""DPDP anonymize.

Domain crm / application dpdp-compliance-service.
Anonymize a customer under DPDP erasure.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='dpdp-compliance-service',
    slug='dpdp-anonymize',
    title='DPDP anonymize',
    mission='Anonymize a customer under DPDP erasure.',
    tools=('dpdp-compliance-service.anonymize_customer',),
    keywords=('anonymize', 'erasure', 'right to forget'),
)
