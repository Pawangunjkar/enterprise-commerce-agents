"""Bulk import ops.

Domain mec / application bulk-catalog-import-service.
Bulk catalog import worker probe.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='bulk-catalog-import-service',
    slug='bulk-import-ops',
    title='Bulk import ops',
    mission='Bulk catalog import worker probe.',
    tools=('bulk-catalog-import-service.health',),
    keywords=('bulk import', 'catalog import'),
)
