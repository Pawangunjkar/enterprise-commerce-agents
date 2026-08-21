"""Map business agents to the FastMCP servers in enterprise-commerce-mcps."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AgentSpec:
    key: str
    title: str
    mission: str
    servers: tuple[str, ...]
    keywords: tuple[str, ...]
    default_scenario: str


AGENTS: dict[str, AgentSpec] = {
    "checkout": AgentSpec(
        key="checkout",
        title="Checkout concierge",
        mission="Pincode serviceability, catalog, ATP, GST quote, place order saga, BharatQR.",
        servers=(
            "pincode-master-service",
            "product-service",
            "cart-service",
            "atp-inventory-service",
            "gst-tax-engine",
            "order-orchestrator",
            "payment-gateway-service",
        ),
        keywords=("checkout", "order", "cart", "pincode", "edd", "upi", "cod", "bharatqr", "place order"),
        default_scenario="checkout-delhi-upi",
    ),
    "tax": AgentSpec(
        key="tax",
        title="GST and TCS desk",
        mission="Live CGST/SGST vs IGST, e-way bill threshold, TCS 194O on GMV.",
        servers=("gst-tax-engine", "tcs-tds-compliance-engine"),
        keywords=("gst", "igst", "cgst", "sgst", "hsn", "eway", "e-way", "tcs", "194o", "tax"),
        default_scenario="gst-interstate-eway",
    ),
    "merchandising": AgentSpec(
        key="merchandising",
        title="Assisted merchandiser",
        mission="Live catalog plus OMS cross-sell / up-sell ranking for a cart.",
        servers=("product-service", "order-orchestrator", "offer-promotion-service"),
        keywords=("recommend", "cross-sell", "upsell", "up-sell", "affinity", "offer", "sku", "catalog"),
        default_scenario="merchandising-upsell",
    ),
    "fulfillment": AgentSpec(
        key="fulfillment",
        title="Fulfillment ops",
        mission="ATP lock, WMS wave, NDR reattempt - warehouse actions, not FAQs.",
        servers=("atp-inventory-service", "wms-fulfillment-service", "ndr-returns-rma-service"),
        keywords=("atp", "stock", "warehouse", "wms", "wave", "pick", "ndr", "rma", "awb"),
        default_scenario="fulfillment-atp-wave",
    ),
    "billing": AgentSpec(
        key="billing",
        title="Collections and invoicing",
        mission="Authorize/QR payments, GST invoices, dunning schedule from billing APIs.",
        servers=("payment-gateway-service", "invoice-service", "dunning-service", "gst-tax-engine"),
        keywords=("invoice", "payment", "qr", "dunning", "collections", "capture", "void"),
        default_scenario="billing-invoice-dunning",
    ),
    "crm": AgentSpec(
        key="crm",
        title="Customer 360 ops",
        mission="OTP, profile, tickets, loyalty, cart recovery, DPDP consent - CRM APIs.",
        servers=(
            "customer-360-service",
            "support-ticket-service",
            "loyalty-rewards-service",
            "cart-abandonment-service",
            "dpdp-compliance-service",
        ),
        keywords=("customer", "otp", "ticket", "loyalty", "dpdp", "consent", "abandon", "crm"),
        default_scenario="crm-otp-ticket-loyalty",
    ),
}


def mcp_module(server: str) -> str:
    return "ecs_mcps." + server.replace("-", "_")


def route_agent(text: str) -> str:
    blob = text.lower()
    scored: list[tuple[int, str]] = []
    for key, spec in AGENTS.items():
        hits = sum(1 for word in spec.keywords if word in blob)
        scored.append((hits, key))
    scored.sort(key=lambda item: (-item[0], item[1]))
    if scored[0][0] == 0:
        return "checkout"
    return scored[0][1]
