"""DLQ replay.

Domain platform / application kafka-dlq-manager.
Replay a dead-letter record into the bus.
"""

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
