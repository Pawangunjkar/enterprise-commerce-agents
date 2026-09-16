"""Payment webhooks LangGraph agent.

Domain `billing` / application `webhook-reconciliation-service`.
Ingest PSP webhook payloads.
"""

from ecs_agents.agents.base import CommerceAgent
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


class WebhookIngestAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `webhook-reconciliation-service`. Ingest PSP webhook payloads. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = WebhookIngestAgent()
