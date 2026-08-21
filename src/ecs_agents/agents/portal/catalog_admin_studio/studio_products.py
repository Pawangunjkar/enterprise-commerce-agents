"""Catalog studio products.

Domain portal / application catalog-admin-studio.
Merchandiser product list in catalog studio.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='catalog-admin-studio',
    slug='studio-products',
    title='Catalog studio products',
    mission='Merchandiser product list in catalog studio.',
    tools=('catalog-admin-studio.list_products',),
    keywords=('catalog studio', 'studio products'),
)
