"""DLQ replay LangGraph agent.

Domain `platform` / application `kafka-dlq-manager`.
Replay a dead-letter record into the bus.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='kafka-dlq-manager',
    slug='dlq-replay',
    title='DLQ replay',
    mission='Replay a dead-letter record into the bus.',
    tools=('kafka-dlq-manager.replay',),
    keywords=('replay dlq', 'dlq replay'),
)


class DlqReplayAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `kafka-dlq-manager`. Replay a dead-letter record into the bus. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = DlqReplayAgent()
