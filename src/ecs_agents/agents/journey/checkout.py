"""Journey: checkout.

Domain journey / application *.
Pincode, catalog, ATP, GST, saga, BharatQR across OMS + billing + platform.
"""

from ecs_agents.agents.spec import journey

SPEC = journey(
    slug='checkout',
    title='Journey: checkout',
    mission='Pincode, catalog, ATP, GST, saga, BharatQR across OMS + billing + platform.',
    tools=('pincode-master-service.serviceability', 'product-service.list_products', 'cart-service.add_cart_item', 'atp-inventory-service.lock_stock', 'gst-tax-engine.compute_gst', 'order-orchestrator.place_order', 'payment-gateway-service.create_bharat_qr', 'suite.recommend_skus', 'suite.get_order'),
    keywords=('checkout', 'place order', 'full checkout'),
    scenario='checkout-delhi-upi',
)
