"""Support ticket.

Domain crm / application support-ticket-service.
Open a live support ticket.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='support-ticket-service',
    slug='ticket-create',
    title='Support ticket',
    mission='Open a live support ticket.',
    tools=('support-ticket-service.create_ticket',),
    keywords=('create ticket', 'support ticket'),
)
