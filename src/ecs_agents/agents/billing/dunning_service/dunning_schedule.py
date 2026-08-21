"""Dunning schedule.

Domain billing / application dunning-service.
Read the live collections/dunning calendar.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='dunning-service',
    slug='dunning-schedule',
    title='Dunning schedule',
    mission='Read the live collections/dunning calendar.',
    tools=('dunning-service.dunning_schedule',),
    keywords=('dunning', 'collections calendar'),
)
