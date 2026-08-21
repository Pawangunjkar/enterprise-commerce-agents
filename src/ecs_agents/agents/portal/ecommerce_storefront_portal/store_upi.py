"""Storefront UPI.

Domain portal / application ecommerce-storefront-portal.
Buyer BharatQR from the storefront checkout.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='ecommerce-storefront-portal',
    slug='store-upi',
    title='Storefront UPI',
    mission='Buyer BharatQR from the storefront checkout.',
    tools=('ecommerce-storefront-portal.create_upi_qr',),
    keywords=('storefront upi', 'store qr'),
)
