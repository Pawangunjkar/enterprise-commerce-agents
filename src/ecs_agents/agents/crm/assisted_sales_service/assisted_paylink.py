"""Assisted pay-link.

Domain crm / application assisted-sales-service.
Create a store-assisted payment link.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='assisted-sales-service',
    slug='assisted-paylink',
    title='Assisted pay-link',
    mission='Create a store-assisted payment link.',
    tools=('assisted-sales-service.create_paylink',),
    keywords=('paylink', 'assisted sales', 'store associate'),
)
