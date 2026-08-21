"""Gateway info.

Domain platform / application api-gateway.
Read gateway build/info from the edge.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='api-gateway',
    slug='info',
    title='Gateway info',
    mission='Read gateway build/info from the edge.',
    tools=('api-gateway.info',),
    keywords=('gateway info', 'gateway version'),
)
