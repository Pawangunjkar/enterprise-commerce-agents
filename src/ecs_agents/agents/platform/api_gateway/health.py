"""Gateway health.

Domain platform / application api-gateway.
Probe gateway liveness before other MCP calls.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='api-gateway',
    slug='health',
    title='Gateway health',
    mission='Probe gateway liveness before other MCP calls.',
    tools=('api-gateway.health',),
    keywords=('gateway health', 'gateway up'),
)
