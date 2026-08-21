"""Storefront EDD.

Domain portal / application ecommerce-storefront-portal.
Buyer EDD check from the storefront.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='ecommerce-storefront-portal',
    slug='store-edd',
    title='Storefront EDD',
    mission='Buyer EDD check from the storefront.',
    tools=('ecommerce-storefront-portal.check_edd',),
    keywords=('storefront edd', 'check edd'),
)
