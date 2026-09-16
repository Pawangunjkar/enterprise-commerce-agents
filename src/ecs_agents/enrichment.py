"""Reusable multi-MCP enrichment playbooks for CRM, OMS, and MEC end-to-end flows.

Enrichment = calling multiple MCP tools in business order to assemble live context
(customer dossier, checkout basket, catalog readiness) before the primary action.

Agents reference these playbooks in their instructions; scenarios execute them as YAML steps.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ecs_agents.mcp_hub import McpHub


@dataclass(frozen=True)
class EnrichmentStep:
    """One MCP call in an enrichment playbook."""

    call: str
    purpose: str
    args: dict[str, Any] | None = None


@dataclass(frozen=True)
class EnrichmentPlaybook:
    """Ordered enrichment steps for a domain flow."""

    id: str
    domain: str
    title: str
    steps: tuple[EnrichmentStep, ...]

    def prompt_lines(self) -> str:
        lines = [f"Enrichment playbook `{self.id}` ({self.title}):"]
        for index, step in enumerate(self.steps, start=1):
            lines.append(f"  {index}. {step.call} — {step.purpose}")
        return "\n".join(lines)


CRM_FULL_PLAYBOOK = EnrichmentPlaybook(
    id="crm-full",
    domain="crm",
    title="OTP → profile → consent → loyalty → hierarchy → address → ticket",
    steps=(
        EnrichmentStep("customer-360-service.otp_start", "Start OTP for mobile identity"),
        EnrichmentStep("customer-360-service.otp_verify", "Verify OTP (lab default 123456)"),
        EnrichmentStep("customer-360-service.upsert_profile", "Persist KYC name/PAN/GSTIN"),
        EnrichmentStep("customer-360-service.get_profile", "Load enriched profile dossier"),
        EnrichmentStep("dpdp-compliance-service.record_consent", "Record DPDP consent purpose"),
        EnrichmentStep("loyalty-rewards-service.get_loyalty", "Fetch loyalty tier and points"),
        EnrichmentStep("account-hierarchy-service.account_tree", "Load B2B account hierarchy"),
        EnrichmentStep("contact-address-service.autofill_address", "Autofill address from pincode"),
        EnrichmentStep("support-ticket-service.create_ticket", "Open support ticket if needed"),
        EnrichmentStep("cart-abandonment-service.mark_abandoned", "Mark cart recovery if applicable"),
    ),
)

CRM_ASSISTED_SALES_PLAYBOOK = EnrichmentPlaybook(
    id="crm-assisted-sales",
    domain="crm",
    title="Profile + consent + pay-link for assisted desk",
    steps=(
        EnrichmentStep("customer-360-service.get_profile", "Load customer dossier"),
        EnrichmentStep("loyalty-rewards-service.get_loyalty", "Check loyalty for discount"),
        EnrichmentStep("dpdp-compliance-service.record_consent", "Record assisted-sales consent"),
        EnrichmentStep("assisted-sales-service.create_paylink", "Mint assisted pay-link"),
    ),
)

OMS_CHECKOUT_PLAYBOOK = EnrichmentPlaybook(
    id="oms-checkout",
    domain="oms",
    title="Pincode → catalog → cart → ATP → price → GST → order → QR → payment",
    steps=(
        EnrichmentStep("pincode-master-service.serviceability", "Check pincode EDD and ODA"),
        EnrichmentStep("product-service.list_products", "Browse catalog SKUs"),
        EnrichmentStep("cart-service.add_cart_item", "Add SKU to cart with unit price"),
        EnrichmentStep("atp-inventory-service.lock_stock", "Lock ATP at warehouse"),
        EnrichmentStep("dynamic-price-engine.calculate_price", "Apply offer/loyalty pricing"),
        EnrichmentStep("gst-tax-engine.compute_gst", "Compute CGST/SGST or IGST"),
        EnrichmentStep("suite.recommend_skus", "Attach cross-sell recommendations"),
        EnrichmentStep("order-orchestrator.place_order", "Run checkout saga"),
        EnrichmentStep("suite.get_order", "Fetch placed order status"),
        EnrichmentStep("payment-gateway-service.create_bharat_qr", "Mint BharatQR for UPI"),
        EnrichmentStep("payment-gateway-service.simulate_success", "Confirm payment (lab)"),
    ),
)

OMS_FULFILLMENT_PLAYBOOK = EnrichmentPlaybook(
    id="oms-fulfillment",
    domain="oms",
    title="Order → ATP lock → WMS wave → carrier waybill → NDR",
    steps=(
        EnrichmentStep("suite.get_order", "Load order details from prior checkout"),
        EnrichmentStep("atp-inventory-service.lock_stock", "Lock stock for fulfillment"),
        EnrichmentStep("wms-fulfillment-service.create_wave", "Release WMS pick wave"),
        EnrichmentStep("carrier-logistics-service.check_serviceability", "Check carrier lane"),
        EnrichmentStep("carrier-logistics-service.create_waybill", "Create AWB/waybill"),
        EnrichmentStep("ndr-returns-rma-service.ndr_action", "Handle NDR reattempt if needed"),
    ),
)

MEC_CATALOG_PLAYBOOK = EnrichmentPlaybook(
    id="mec-catalog-lifecycle",
    domain="mec",
    title="Create SKU → activate → IMEI → search index",
    steps=(
        EnrichmentStep("product-service.create_product", "Create draft SKU with HSN"),
        EnrichmentStep("product-service.activate_product", "Activate SKU to live catalog"),
        EnrichmentStep("serial-imei-tracking-service.ingest_imei", "Ingest IMEI for handset SKU"),
        EnrichmentStep("product-service.list_products", "Verify SKU appears in catalog"),
        EnrichmentStep("search-solr-indexer.search_products", "Confirm faceted search index"),
    ),
)

MEC_B2B_PLAYBOOK = EnrichmentPlaybook(
    id="mec-b2b-quote",
    domain="mec",
    title="Account tree → B2B tier quote → bundle price → CPQ",
    steps=(
        EnrichmentStep("account-hierarchy-service.account_tree", "Load dealer/distributor tree"),
        EnrichmentStep("b2b-tiered-catalog-service.b2b_quote", "Quote tier price for account"),
        EnrichmentStep("component-bundle-service.price_bundle", "Price component bundle"),
        EnrichmentStep("cpq-rule-engine.evaluate_cpq", "Evaluate CPQ rules on quote"),
    ),
)

MEC_OFFER_PLAYBOOK = EnrichmentPlaybook(
    id="mec-offer-promo",
    domain="mec",
    title="Schema validate → CPQ → offer → temporal activation",
    steps=(
        EnrichmentStep("dynamic-schema-engine.validate_schema", "Validate offer payload schema"),
        EnrichmentStep("cpq-rule-engine.evaluate_cpq", "Run CPQ evaluation"),
        EnrichmentStep("offer-promotion-service.create_offer", "Create promotional offer"),
        EnrichmentStep("temporal-activation-service.time_travel", "Preview catalog at activation time"),
    ),
)

PLAYBOOKS: dict[str, EnrichmentPlaybook] = {
    p.id: p
    for p in (
        CRM_FULL_PLAYBOOK,
        CRM_ASSISTED_SALES_PLAYBOOK,
        OMS_CHECKOUT_PLAYBOOK,
        OMS_FULFILLMENT_PLAYBOOK,
        MEC_CATALOG_PLAYBOOK,
        MEC_B2B_PLAYBOOK,
        MEC_OFFER_PLAYBOOK,
    )
}


def playbook_prompt(playbook_id: str) -> str:
    """Return enrichment instructions for agent system prompts."""
    playbook = PLAYBOOKS.get(playbook_id)
    if not playbook:
        return ""
    return (
        f"When the user asks for a full end-to-end {playbook.domain.upper()} flow, "
        f"call MCP tools in this order (enrichment before the final action):\n"
        f"{playbook.prompt_lines()}\n"
        "Pass outputs from earlier steps into later tool args (orderId, customerId, sku, cartId). "
        "Stop and report the MCP error payload if any step fails."
    )


async def run_playbook(
    hub: McpHub,
    playbook_id: str,
    *,
    args_by_step: dict[str, dict[str, Any]] | None = None,
    ctx: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Execute an enrichment playbook programmatically (used by tests and tooling)."""
    playbook = PLAYBOOKS.get(playbook_id)
    if not playbook:
        raise KeyError(f"Unknown playbook '{playbook_id}'")

    args_by_step = args_by_step or {}
    context = ctx or {}
    steps_out: list[dict[str, Any]] = []

    servers = {step.call.split(".", 1)[0] for step in playbook.steps if not step.call.startswith("suite.")}
    await hub.start(tuple(servers))

    for index, step in enumerate(playbook.steps, start=1):
        arguments = args_by_step.get(step.call, step.args or {})
        result = await hub.call(step.call, arguments)
        step_id = f"step{index}"
        context[step_id] = result
        context["last"] = result
        steps_out.append({"id": step_id, "call": step.call, "args": arguments, "result": result})
        if isinstance(result, dict) and result.get("error"):
            return {"playbook": playbook_id, "ok": False, "failed_step": step_id, "steps": steps_out}

    return {"playbook": playbook_id, "ok": True, "title": playbook.title, "steps": steps_out, "context": context}
