"""Catalog studio time-travel.

Domain portal / application catalog-admin-studio.
As-of catalog from catalog studio.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='catalog-admin-studio',
    slug='studio-temporal',
    title='Catalog studio time-travel',
    mission='As-of catalog from catalog studio.',
    tools=('catalog-admin-studio.time_travel',),
    keywords=('studio time travel',),
)
