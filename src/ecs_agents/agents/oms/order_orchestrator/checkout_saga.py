"""Checkout saga.

Domain oms / application order-orchestrator.
Place an order through ATP, pay/COD, WMS, capture saga.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='order-orchestrator',
    slug='checkout-saga',
    title='Checkout saga',
    mission='Place an order through ATP, pay/COD, WMS, capture saga.',
    tools=('order-orchestrator.place_order', 'suite.get_order'),
    keywords=('place order', 'checkout saga', 'order saga'),
    scenario='checkout-delhi-upi',
)
