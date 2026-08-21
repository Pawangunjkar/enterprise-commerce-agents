"""Checkout intent.

Domain oms / application checkout-service.
Create a checkout intent (pincode, GSTIN, payment mode).
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='checkout-service',
    slug='checkout-intent',
    title='Checkout intent',
    mission='Create a checkout intent (pincode, GSTIN, payment mode).',
    tools=('checkout-service.create_checkout_intent',),
    keywords=('checkout intent', 'gstin checkout'),
)
