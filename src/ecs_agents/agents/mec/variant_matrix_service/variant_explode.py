"""Variant matrix.

Domain mec / application variant-matrix-service.
Explode RAM/color/storage variant combinations.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='variant-matrix-service',
    slug='variant-explode',
    title='Variant matrix',
    mission='Explode RAM/color/storage variant combinations.',
    tools=('variant-matrix-service.explode_variants',),
    keywords=('variant', 'variant matrix', 'explode'),
)
