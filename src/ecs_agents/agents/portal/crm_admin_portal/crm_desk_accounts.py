"""CRM admin accounts.

Domain portal / application crm-admin-portal.
Account tree from CRM admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='crm-admin-portal',
    slug='crm-desk-accounts',
    title='CRM admin accounts',
    mission='Account tree from CRM admin.',
    tools=('crm-admin-portal.account_tree',),
    keywords=('crm admin tree',),
)
