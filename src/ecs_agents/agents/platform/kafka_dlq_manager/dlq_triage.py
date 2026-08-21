"""DLQ triage.

Domain platform / application kafka-dlq-manager.
List open Kafka dead letters.
"""

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
