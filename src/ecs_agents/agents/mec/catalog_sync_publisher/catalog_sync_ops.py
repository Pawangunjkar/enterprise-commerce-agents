"""Catalog sync ops.

Domain mec / application catalog-sync-publisher.
Outbound catalog sync publisher probe.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='catalog-sync-publisher',
    slug='catalog-sync-ops',
    title='Catalog sync ops',
    mission='Outbound catalog sync publisher probe.',
    tools=('catalog-sync-publisher.health',),
    keywords=('catalog sync', 'debezium'),
)
