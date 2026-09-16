"""Build LangChain tools with named fields so ReAct can call MCP APIs properly."""

from __future__ import annotations

import json
from typing import Any

from langchain_core.tools import StructuredTool
from pydantic import Field, create_model

from ecs_agents.mcp_hub import McpHub
from ecs_agents.suite_http import dump

FIELDS: dict[str, tuple[str, ...]] = {
    "api-gateway.health": (),
    "api-gateway.info": (),
    "search-solr-indexer.search_products": ("q", "brand", "ram", "color", "minPrice", "maxPrice", "start", "rows"),
    "search-solr-indexer.autocomplete": ("q",),
    "pincode-master-service.get_pincode": ("pincode",),
    "pincode-master-service.serviceability": ("pincode", "origin"),
    "kafka-dlq-manager.list_dlq": ("status", "page", "size"),
    "kafka-dlq-manager.replay": ("id",),
    "mca-audit-trail-service.append_audit": ("actor", "action", "resourceType", "resourceId"),
    "mca-audit-trail-service.list_audit": ("resourceType", "page", "size"),
    "notification-service.send_notification": ("channel", "to", "template"),
    "product-service.list_products": ("page", "size"),
    "product-service.get_product": ("id",),
    "product-service.create_product": ("sku", "name", "hsnCode", "brand", "categoryPath", "listPriceInr"),
    "product-service.activate_product": ("id",),
    "variant-matrix-service.explode_variants": ("payload",),
    "serial-imei-tracking-service.ingest_imei": ("sku", "imei1", "imei2", "serial"),
    "b2b-tiered-catalog-service.b2b_quote": ("payload",),
    "component-bundle-service.price_bundle": ("payload",),
    "cpq-rule-engine.evaluate_cpq": ("payload",),
    "dynamic-schema-engine.validate_schema": ("payload",),
    "offer-promotion-service.create_offer": ("payload",),
    "temporal-activation-service.time_travel": ("asOf",),
    "media-dam-service.health": (),
    "bulk-catalog-import-service.health": (),
    "catalog-sync-publisher.health": (),
    "cart-service.get_cart": ("cartId",),
    "cart-service.add_cart_item": ("cartId", "sku", "qty", "unitPrice"),
    "checkout-service.create_checkout_intent": ("cartId", "pincode", "paymentMode", "amount", "gstin"),
    "order-orchestrator.place_order": ("cartId", "pincode", "paymentMode", "amount"),
    "dynamic-price-engine.calculate_price": ("sku", "basePrice", "offerDiscount", "loyaltyDiscount"),
    "atp-inventory-service.lock_stock": ("sku", "qty", "warehouse"),
    "wms-fulfillment-service.create_wave": ("payload",),
    "ondc-seller-gateway.beckn_search": ("payload",),
    "ondc-seller-gateway.beckn_select": ("payload",),
    "ondc-seller-gateway.beckn_init": ("payload",),
    "ondc-seller-gateway.beckn_confirm": ("payload",),
    "ondc-seller-gateway.beckn_status": ("payload",),
    "ondc-seller-gateway.beckn_track": ("payload",),
    "ondc-seller-gateway.beckn_cancel": ("payload",),
    "carrier-logistics-service.check_serviceability": ("carrier", "payload"),
    "carrier-logistics-service.create_waybill": ("carrier", "payload"),
    "bopis-pickup-service.reserve_pickup": ("payload",),
    "ndr-returns-rma-service.ndr_action": ("awb", "action"),
    "catalog-consumer-service.health": (),
    "gst-tax-engine.compute_gst": ("taxable", "slab", "originState", "destState", "hsn"),
    "gst-tax-engine.eway_bill": ("taxable", "slab", "originState", "destState", "hsn"),
    "tcs-tds-compliance-engine.compute_tcs_194o": ("payload",),
    "price-book-service.get_price_book": ("sku",),
    "subscription-emi-service.emi_quote": ("principal", "months"),
    "payment-gateway-service.create_bharat_qr": ("orderId", "amount", "vpa", "merchantName", "mcc"),
    "payment-gateway-service.payment_status": ("txnId",),
    "payment-gateway-service.simulate_success": ("txnId",),
    "payment-gateway-plugins.health": (),
    "cod-remittance-reconcile-service.match_cod": ("awb", "carrierAmount", "bankAmount"),
    "webhook-reconciliation-service.ingest_webhook": ("provider",),
    "invoice-service.issue_invoice": ("payload",),
    "general-ledger-service.post_journal": ("payload",),
    "dunning-service.dunning_schedule": (),
    "customer-360-service.otp_start": ("mobile",),
    "customer-360-service.otp_verify": ("mobile", "otp"),
    "customer-360-service.upsert_profile": ("mobile", "pan", "gstin", "name"),
    "customer-360-service.get_profile": ("mobile",),
    "assisted-sales-service.create_paylink": ("payload",),
    "account-hierarchy-service.account_tree": (),
    "contact-address-service.autofill_address": ("pincode",),
    "support-ticket-service.create_ticket": ("payload",),
    "loyalty-rewards-service.get_loyalty": ("customerId", "festivalMultiplier"),
    "cart-abandonment-service.mark_abandoned": ("payload",),
    "dpdp-compliance-service.record_consent": ("payload",),
    "dpdp-compliance-service.anonymize_customer": ("customerId",),
    "ecommerce-storefront-portal.search_store": ("q", "brand", "start", "rows"),
    "ecommerce-storefront-portal.check_edd": ("pincode",),
    "ecommerce-storefront-portal.create_upi_qr": ("orderId", "amount", "vpa", "merchantName", "mcc"),
    "master-admin-portal.list_dlq": ("status", "page", "size"),
    "master-admin-portal.replay_dlq": ("id",),
    "master-admin-portal.list_audit": ("resourceType", "page", "size"),
    "catalog-admin-studio.list_products": ("page", "size"),
    "catalog-admin-studio.ingest_imei": ("sku", "imei1", "imei2", "serial"),
    "catalog-admin-studio.time_travel": ("asOf",),
    "order-admin-portal.place_order": ("cartId", "pincode", "paymentMode", "amount"),
    "order-admin-portal.create_wave": ("payload",),
    "order-admin-portal.ndr_action": ("awb", "action"),
    "billing-admin-portal.compute_gst": ("taxable", "slab", "originState", "destState", "hsn"),
    "billing-admin-portal.compute_tcs_194o": ("payload",),
    "billing-admin-portal.post_journal": ("payload",),
    "crm-admin-portal.otp_start": ("mobile",),
    "crm-admin-portal.create_ticket": ("payload",),
    "crm-admin-portal.account_tree": (),
    "crm-admin-portal.record_consent": ("payload",),
    "suite.recommend_skus": ("skus", "limit"),
    "suite.get_order": ("orderId",),
}


def mcp_tools(hub: McpHub, qualified_names: list[str]) -> list[StructuredTool]:
    return [_tool(hub, name) for name in qualified_names]


def _tool(hub: McpHub, qualified: str) -> StructuredTool:
    fields = FIELDS.get(qualified, ("payload",))
    annotations: dict[str, Any] = {}
    for field in fields:
        annotations[field] = (Any, Field(default=None, description=field))
    if not annotations:
        annotations["confirm"] = (bool, Field(default=True, description="Invoke this no-argument MCP tool"))
    model = create_model(qualified.replace(".", "_").replace("-", "_")[:50], **annotations)

    async def invoke(**kwargs: Any) -> str:
        body = {key: value for key, value in kwargs.items() if value is not None and key != "confirm"}
        raw = body.get("payload")
        if isinstance(raw, str):
            try:
                body["payload"] = json.loads(raw)
            except json.JSONDecodeError:
                pass
        return dump(await hub.call(qualified, body))

    safe = qualified.replace(".", "__").replace("-", "_")[:64]
    return StructuredTool.from_function(
        coroutine=invoke,
        name=safe,
        description=f"Live MCP `{qualified}` on Enterprise Commerce Suite. Named business fields. Returns JSON.",
        args_schema=model,
    )
