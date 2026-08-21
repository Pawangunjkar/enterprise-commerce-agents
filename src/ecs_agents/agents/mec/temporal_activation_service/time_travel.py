"""Temporal catalog.

Domain mec / application temporal-activation-service.
Read catalog as-of a timestamp.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='temporal-activation-service',
    slug='time-travel',
    title='Temporal catalog',
    mission='Read catalog as-of a timestamp.',
    tools=('temporal-activation-service.time_travel',),
    keywords=('time travel', 'as-of', 'temporal'),
)
