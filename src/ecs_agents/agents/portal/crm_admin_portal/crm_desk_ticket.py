"""CRM admin ticket.

Domain portal / application crm-admin-portal.
Assisted ticket from CRM admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='crm-admin-portal',
    slug='crm-desk-ticket',
    title='CRM admin ticket',
    mission='Assisted ticket from CRM admin.',
    tools=('crm-admin-portal.create_ticket',),
    keywords=('crm admin ticket',),
)
