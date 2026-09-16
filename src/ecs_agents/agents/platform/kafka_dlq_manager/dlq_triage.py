"""DLQ triage LangGraph agent.

Domain `platform` / application `kafka-dlq-manager`.
List open Kafka dead letters.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='kafka-dlq-manager',
    slug='dlq-triage',
    title='DLQ triage',
    mission='List open Kafka dead letters.',
    tools=('kafka-dlq-manager.list_dlq',),
    keywords=('dlq', 'dead letter'),
)


class DlqTriageAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `kafka-dlq-manager`. List open Kafka dead letters. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = DlqTriageAgent()
