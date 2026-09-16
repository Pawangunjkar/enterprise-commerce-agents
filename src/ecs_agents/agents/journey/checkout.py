"""Journey: checkout LangGraph agent.

Domain `journey` / application `*`.
Pincode, catalog, ATP, GST, saga, BharatQR across OMS + billing + platform.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import journey
from ecs_agents.enrichment import playbook_prompt

SPEC = journey(
    slug="checkout",
    title="Journey: checkout",
    mission="Pincode, catalog, cart, ATP, price, GST, saga, BharatQR, payment confirm.",
    tools=(
        "pincode-master-service.serviceability",
        "product-service.list_products",
        "cart-service.add_cart_item",
        "atp-inventory-service.lock_stock",
        "dynamic-price-engine.calculate_price",
        "gst-tax-engine.compute_gst",
        "order-orchestrator.place_order",
        "payment-gateway-service.create_bharat_qr",
        "payment-gateway-service.simulate_success",
        "suite.recommend_skus",
        "suite.get_order",
    ),
    keywords=("checkout", "place order", "full checkout", "delhi upi"),
    scenario="checkout-delhi-upi",
)


class CheckoutAgent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You own the OMS checkout journey from pincode serviceability through payment capture. "
        "Pass cartId, orderId, sku, and amounts from earlier MCP steps into later tools. "
        + playbook_prompt("oms-checkout")
    )


AGENT = CheckoutAgent()
