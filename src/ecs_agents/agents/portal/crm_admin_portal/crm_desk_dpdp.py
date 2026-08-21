"""CRM admin DPDP.

Domain portal / application crm-admin-portal.
Consent capture from CRM admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='crm-admin-portal',
    slug='crm-desk-dpdp',
    title='CRM admin DPDP',
    mission='Consent capture from CRM admin.',
    tools=('crm-admin-portal.record_consent',),
    keywords=('crm admin dpdp',),
)
