"""Checkout saga LangGraph agent.

Domain `oms` / application `order-orchestrator`.
Place an order through ATP, pay/COD, WMS, capture saga.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist
from ecs_agents.enrichment import playbook_prompt

SPEC = specialist(
    domain="oms",
    application="order-orchestrator",
    slug="checkout-saga",
    title="Checkout saga",
    mission="Place an order through cart, ATP, pricing, GST, saga, and payment confirm.",
    tools=(
        "cart-service.add_cart_item",
        "atp-inventory-service.lock_stock",
        "dynamic-price-engine.calculate_price",
        "gst-tax-engine.compute_gst",
        "order-orchestrator.place_order",
        "payment-gateway-service.create_bharat_qr",
        "payment-gateway-service.simulate_success",
        "suite.get_order",
    ),
    keywords=("place order", "checkout saga", "order saga"),
    scenario="checkout-delhi-upi",
)


class CheckoutSagaAgent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You are the order-orchestrator checkout operator. Enrich with cart + ATP + price + GST "
        "before place_order, then mint BharatQR and simulate_success in lab. "
        + playbook_prompt("oms-checkout")
    )


AGENT = CheckoutSagaAgent()
