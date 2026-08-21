"""Payment webhooks.

Domain billing / application webhook-reconciliation-service.
Ingest PSP webhook payloads.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='webhook-reconciliation-service',
    slug='webhook-ingest',
    title='Payment webhooks',
    mission='Ingest PSP webhook payloads.',
    tools=('webhook-reconciliation-service.ingest_webhook',),
    keywords=('payment webhook', 'psp webhook'),
)
