"""Product lifecycle.

Domain mec / application product-service.
Create and activate SKUs (draft to live).
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='product-service',
    slug='catalog-lifecycle',
    title='Product lifecycle',
    mission='Create and activate SKUs (draft to live).',
    tools=('product-service.create_product', 'product-service.activate_product'),
    keywords=('create product', 'activate sku', 'product lifecycle'),
)
