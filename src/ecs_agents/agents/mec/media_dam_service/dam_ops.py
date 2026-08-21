"""DAM ops.

Domain mec / application media-dam-service.
Media/DAM service health and ops probe.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='media-dam-service',
    slug='dam-ops',
    title='DAM ops',
    mission='Media/DAM service health and ops probe.',
    tools=('media-dam-service.health',),
    keywords=('dam', 'media asset'),
)
