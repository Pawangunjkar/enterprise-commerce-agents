"""Catalog studio IMEI.

Domain portal / application catalog-admin-studio.
IMEI ingest from catalog studio.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='catalog-admin-studio',
    slug='studio-imei',
    title='Catalog studio IMEI',
    mission='IMEI ingest from catalog studio.',
    tools=('catalog-admin-studio.ingest_imei',),
    keywords=('studio imei',),
)
