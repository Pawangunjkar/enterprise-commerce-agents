"""Per-domain, per-application LangGraph agents.

Every Enterprise Commerce Suite application (MCP server) has at least one specialist.
Applications with more than one business job get multiple agents.
Journey squads stitch several apps for end-to-end playbooks.
"""

from __future__ import annotations

from dataclasses import dataclass


DOMAINS = (
    "platform",
    "mec",
    "oms",
    "billing",
    "crm",
    "portal",
    "journey",
)


@dataclass(frozen=True)
class AgentSpec:
    key: str
    domain: str
    application: str
    slug: str
    title: str
    mission: str
    tools: tuple[str, ...]
    keywords: tuple[str, ...]
    default_scenario: str = ""
    kind: str = "specialist"  # specialist | journey

    @property
    def servers(self) -> tuple[str, ...]:
        seen: list[str] = []
        for tool in self.tools:
            if tool.startswith("suite."):
                continue
            app = tool.split(".", 1)[0]
            if app not in seen:
                seen.append(app)
        if not seen and self.application not in {"", "*"}:
            seen.append(self.application)
        return tuple(seen)


def _q(app: str, tools: tuple[str, ...]) -> tuple[str, ...]:
    out: list[str] = []
    for tool in tools:
        out.append(tool if "." in tool else f"{app}.{tool}")
    return tuple(out)


def _spec(
    domain: str,
    app: str,
    slug: str,
    title: str,
    mission: str,
    tools: tuple[str, ...],
    keywords: tuple[str, ...],
    scenario: str = "",
    kind: str = "specialist",
) -> AgentSpec:
    return AgentSpec(
        key=f"{domain}.{app}.{slug}",
        domain=domain,
        application=app,
        slug=slug,
        title=title,
        mission=mission,
        tools=_q(app, tools),
        keywords=keywords,
        default_scenario=scenario,
        kind=kind,
    )


def _build() -> dict[str, AgentSpec]:
    rows: list[AgentSpec] = []

    def add(*args, **kwargs) -> None:
        rows.append(_spec(*args, **kwargs))

    # --- platform ---
    add("platform", "api-gateway", "health", "Gateway health",
        "Probe gateway liveness before other MCP calls.",
        ("health",), ("gateway health", "gateway up"))
    add("platform", "api-gateway", "info", "Gateway info",
        "Read gateway build/info from the edge.",
        ("info",), ("gateway info", "gateway version"))
    add("platform", "search-solr-indexer", "faceted-search", "Solr faceted search",
        "Live product search with brand/RAM/price facets.",
        ("search_products",), ("solr", "faceted search", "search products"))
    add("platform", "search-solr-indexer", "autocomplete", "Search autocomplete",
        "Typeahead from the Solr products collection.",
        ("autocomplete",), ("autocomplete", "typeahead"))
    add("platform", "pincode-master-service", "pincode-lookup", "Pincode master lookup",
        "Load India pincode master attributes.",
        ("get_pincode",), ("pincode lookup", "pincode master"))
    add("platform", "pincode-master-service", "serviceability", "Serviceability and EDD",
        "Origin vs destination serviceability, ODA, EDD.",
        ("serviceability",), ("serviceability", "edd", "oda"))
    add("platform", "kafka-dlq-manager", "dlq-triage", "DLQ triage",
        "List open Kafka dead letters.",
        ("list_dlq",), ("dlq", "dead letter"))
    add("platform", "kafka-dlq-manager", "dlq-replay", "DLQ replay",
        "Replay a dead-letter record into the bus.",
        ("replay",), ("replay dlq", "dlq replay"))
    add("platform", "mca-audit-trail-service", "audit-append", "MCA audit append",
        "Write an MCA-style audit event.",
        ("append_audit",), ("append audit", "audit write"))
    add("platform", "mca-audit-trail-service", "audit-query", "MCA audit query",
        "Page audit events by resource type.",
        ("list_audit",), ("list audit", "audit trail"))
    add("platform", "notification-service", "notify", "Notification dispatch",
        "Send SMS/email/WhatsApp templates (OTP, order).",
        ("send_notification",), ("sms", "whatsapp", "notification"))

    # --- master enterprise catalog ---
    add("mec", "product-service", "catalog-browse", "Product browse",
        "List and fetch live SKUs from product-service.",
        ("list_products", "get_product"), ("list products", "get product", "sku browse"))
    add("mec", "product-service", "catalog-lifecycle", "Product lifecycle",
        "Create and activate SKUs (draft to live).",
        ("create_product", "activate_product"), ("create product", "activate sku", "product lifecycle"))
    add("mec", "variant-matrix-service", "variant-explode", "Variant matrix",
        "Explode RAM/color/storage variant combinations.",
        ("explode_variants",), ("variant", "variant matrix", "explode"))
    add("mec", "serial-imei-tracking-service", "imei-ingest", "IMEI ingest",
        "Ingest 15-digit IMEI with Luhn checks.",
        ("ingest_imei",), ("imei", "serial ingest", "luhn"))
    add("mec", "b2b-tiered-catalog-service", "b2b-quote", "B2B tier quote",
        "Quote a dealer/distributor tier price.",
        ("b2b_quote",), ("b2b", "dealer price", "tier quote"))
    add("mec", "component-bundle-service", "bundle-price", "Bundle pricing",
        "Price a component bundle / kit.",
        ("price_bundle",), ("bundle", "kit price"))
    add("mec", "cpq-rule-engine", "cpq-evaluate", "CPQ rules",
        "Evaluate configure-price-quote rules on a payload.",
        ("evaluate_cpq",), ("cpq", "configure price"))
    add("mec", "dynamic-schema-engine", "schema-validate", "Dynamic schema",
        "Validate attribute payloads against catalog schema.",
        ("validate_schema",), ("schema", "attribute validate"))
    add("mec", "offer-promotion-service", "offer-create", "Offer authoring",
        "Create a live promotion/offer.",
        ("create_offer",), ("create offer", "promotion", "festival offer"))
    add("mec", "temporal-activation-service", "time-travel", "Temporal catalog",
        "Read catalog as-of a timestamp.",
        ("time_travel",), ("time travel", "as-of", "temporal"))
    add("mec", "media-dam-service", "dam-ops", "DAM ops",
        "Media/DAM service health and ops probe.",
        ("health",), ("dam", "media asset"))
    add("mec", "bulk-catalog-import-service", "bulk-import-ops", "Bulk import ops",
        "Bulk catalog import worker probe.",
        ("health",), ("bulk import", "catalog import"))
    add("mec", "catalog-sync-publisher", "catalog-sync-ops", "Catalog sync ops",
        "Outbound catalog sync publisher probe.",
        ("health",), ("catalog sync", "debezium"))

    # --- order management ---
    add("oms", "cart-service", "cart-read", "Cart read",
        "Load a cart by id from cart-service.",
        ("get_cart",), ("get cart", "view cart"))
    add("oms", "cart-service", "cart-mutate", "Cart mutate",
        "Add line items to a live cart.",
        ("add_cart_item",), ("add to cart", "cart item"))
    add("oms", "checkout-service", "checkout-intent", "Checkout intent",
        "Create a checkout intent (pincode, GSTIN, payment mode).",
        ("create_checkout_intent",), ("checkout intent", "gstin checkout"))
    add("oms", "order-orchestrator", "checkout-saga", "Checkout saga",
        "Place an order through ATP, pay/COD, WMS, capture saga.",
        ("place_order", "suite.get_order"), ("place order", "checkout saga", "order saga"),
        "checkout-delhi-upi")
    add("oms", "order-orchestrator", "merchandising", "OMS merchandising",
        "Cross-sell and up-sell from affinity rules and SKU ladder.",
        ("suite.recommend_skus",), ("cross-sell", "upsell", "up-sell", "recommend", "affinity"),
        "merchandising-upsell")
    add("oms", "dynamic-price-engine", "price-calculate", "Dynamic price",
        "Calculate offer and loyalty adjusted INR price.",
        ("calculate_price",), ("dynamic price", "calculate price"))
    add("oms", "atp-inventory-service", "atp-lock", "ATP lock",
        "Lock available-to-promise stock in a warehouse.",
        ("lock_stock",), ("atp", "lock stock", "inventory lock"))
    add("oms", "wms-fulfillment-service", "wms-wave", "WMS pick wave",
        "Release a warehouse pick wave.",
        ("create_wave",), ("wms", "pick wave", "warehouse wave"))
    add("oms", "ondc-seller-gateway", "ondc-discovery", "ONDC discovery",
        "Beckn search/select/init on the seller gateway.",
        ("beckn_search", "beckn_select", "beckn_init"), ("ondc search", "beckn search", "beckn select"))
    add("oms", "ondc-seller-gateway", "ondc-order", "ONDC order lifecycle",
        "Beckn confirm, status, track, cancel.",
        ("beckn_confirm", "beckn_status", "beckn_track", "beckn_cancel"),
        ("ondc confirm", "beckn track", "beckn cancel"))
    add("oms", "carrier-logistics-service", "carrier-serviceability", "Carrier serviceability",
        "Ask Delhivery/Shiprocket/BlueDart style serviceability.",
        ("check_serviceability",), ("carrier serviceability", "delhivery", "shiprocket"))
    add("oms", "carrier-logistics-service", "waybill", "Waybill create",
        "Create a carrier waybill/AWB.",
        ("create_waybill",), ("waybill", "awb create", "shipment"))
    add("oms", "bopis-pickup-service", "bopis-reserve", "BOPIS reserve",
        "Reserve buy-online-pickup-in-store inventory.",
        ("reserve_pickup",), ("bopis", "pickup reserve", "click collect"))
    add("oms", "ndr-returns-rma-service", "ndr-ops", "NDR / RMA",
        "Take NDR action (reattempt, rto) on an AWB.",
        ("ndr_action",), ("ndr", "rma", "reattempt", "rto"),
        "fulfillment-atp-wave")
    add("oms", "catalog-consumer-service", "oms-catalog-consumer", "OMS catalog consumer",
        "OMS replica consumer health probe.",
        ("health",), ("catalog consumer", "oms replica"))

    # --- billing ---
    add("billing", "gst-tax-engine", "gst-compute", "GST compute",
        "Intra CGST+SGST vs inter IGST on a taxable value.",
        ("compute_gst",), ("compute gst", "cgst", "sgst", "igst", "gst slab"),
        "gst-interstate-eway")
    add("billing", "gst-tax-engine", "eway-bill", "E-way bill",
        "E-way bill required flag when taxable exceeds threshold.",
        ("eway_bill",), ("e-way", "eway", "e-way bill", "eway bill"))
    add("billing", "tcs-tds-compliance-engine", "tcs-194o", "TCS 194O",
        "Section 194O TCS on e-commerce GMV.",
        ("compute_tcs_194o",), ("tcs", "194o", "194-o"))
    add("billing", "price-book-service", "price-book", "Price book",
        "Read contractual price-book for a SKU.",
        ("get_price_book",), ("price book", "contract price"))
    add("billing", "subscription-emi-service", "emi-quote", "EMI quote",
        "Quote subscription/EMI on principal and tenure.",
        ("emi_quote",), ("emi", "no cost emi", "tenure"))
    add("billing", "payment-gateway-service", "bharat-qr", "BharatQR",
        "Mint dynamic UPI BharatQR and intent URLs.",
        ("create_bharat_qr",), ("bharatqr", "bharat qr", "upi qr"))
    add("billing", "payment-gateway-service", "payment-ops", "Payment ops",
        "Poll payment status or simulate capture.",
        ("payment_status", "simulate_success"), ("payment status", "simulate success", "upi status"))
    add("billing", "payment-gateway-plugins", "plugin-health", "Payment plugin health",
        "Payment plugin process probe.",
        ("health",), ("payment plugin", "psp plugin"))
    add("billing", "cod-remittance-reconcile-service", "cod-match", "COD remittance",
        "Match COD remittance vs carrier and bank amounts.",
        ("match_cod",), ("cod remittance", "cod match"))
    add("billing", "webhook-reconciliation-service", "webhook-ingest", "Payment webhooks",
        "Ingest PSP webhook payloads.",
        ("ingest_webhook",), ("payment webhook", "psp webhook"))
    add("billing", "invoice-service", "invoice-issue", "GST invoice",
        "Issue and persist a GST tax invoice.",
        ("issue_invoice",), ("issue invoice", "tax invoice", "gst invoice"),
        "billing-invoice-dunning")
    add("billing", "general-ledger-service", "ledger-post", "General ledger",
        "Post a GAAP journal entry.",
        ("post_journal",), ("journal", "general ledger", "gaap"))
    add("billing", "dunning-service", "dunning-schedule", "Dunning schedule",
        "Read the live collections/dunning calendar.",
        ("dunning_schedule",), ("dunning", "collections calendar"))

    # --- crm ---
    add("crm", "customer-360-service", "identity-otp", "Customer OTP",
        "Start and verify mobile OTP (live CRM, not FAQ).",
        ("otp_start", "otp_verify"), ("otp", "verify otp", "mobile otp"))
    add("crm", "customer-360-service", "customer-profile", "Customer profile",
        "Upsert PAN/GSTIN/name on the 360 profile.",
        ("upsert_profile",), ("customer profile", "gstin profile", "pan"))
    add("crm", "assisted-sales-service", "assisted-paylink", "Assisted pay-link",
        "Create a store-assisted payment link.",
        ("create_paylink",), ("paylink", "assisted sales", "store associate"))
    add("crm", "account-hierarchy-service", "account-tree", "B2B account tree",
        "Read dealer/distributor account hierarchy.",
        ("account_tree",), ("account tree", "b2b hierarchy"))
    add("crm", "contact-address-service", "address-autofill", "Address autofill",
        "Autofill address from pincode master.",
        ("autofill_address",), ("autofill", "address pincode"))
    add("crm", "support-ticket-service", "ticket-create", "Support ticket",
        "Open a live support ticket.",
        ("create_ticket",), ("create ticket", "support ticket"))
    add("crm", "loyalty-rewards-service", "loyalty-balance", "Loyalty balance",
        "Read loyalty points with festival multiplier.",
        ("get_loyalty",), ("loyalty", "reward points", "festival multiplier"))
    add("crm", "cart-abandonment-service", "cart-recovery", "Cart abandonment",
        "Mark a cart abandoned for recovery journeys.",
        ("mark_abandoned",), ("abandon", "cart recovery"))
    add("crm", "dpdp-compliance-service", "dpdp-consent", "DPDP consent",
        "Record DPDP Act 2023 consent.",
        ("record_consent",), ("dpdp", "consent", "dpdp act"))
    add("crm", "dpdp-compliance-service", "dpdp-anonymize", "DPDP anonymize",
        "Anonymize a customer under DPDP erasure.",
        ("anonymize_customer",), ("anonymize", "erasure", "right to forget"))

    # --- portals (one agent per portal job) ---
    add("portal", "ecommerce-storefront-portal", "store-search", "Storefront search",
        "Buyer-facing Solr search from the storefront portal MCP.",
        ("search_store",), ("storefront search", "store search"))
    add("portal", "ecommerce-storefront-portal", "store-edd", "Storefront EDD",
        "Buyer EDD check from the storefront.",
        ("check_edd",), ("storefront edd", "check edd"))
    add("portal", "ecommerce-storefront-portal", "store-upi", "Storefront UPI",
        "Buyer BharatQR from the storefront checkout.",
        ("create_upi_qr",), ("storefront upi", "store qr"))
    add("portal", "master-admin-portal", "ops-dlq", "Master admin DLQ",
        "Ops DLQ from master admin.",
        ("list_dlq", "replay_dlq"), ("master admin dlq",))
    add("portal", "master-admin-portal", "ops-audit", "Master admin audit",
        "Ops audit query from master admin.",
        ("list_audit",), ("master admin audit",))
    add("portal", "catalog-admin-studio", "studio-products", "Catalog studio products",
        "Merchandiser product list in catalog studio.",
        ("list_products",), ("catalog studio", "studio products"))
    add("portal", "catalog-admin-studio", "studio-imei", "Catalog studio IMEI",
        "IMEI ingest from catalog studio.",
        ("ingest_imei",), ("studio imei",))
    add("portal", "catalog-admin-studio", "studio-temporal", "Catalog studio time-travel",
        "As-of catalog from catalog studio.",
        ("time_travel",), ("studio time travel",))
    add("portal", "order-admin-portal", "order-desk-place", "Order admin place",
        "Ops place-order from order admin.",
        ("place_order",), ("order admin", "ops place order"))
    add("portal", "order-admin-portal", "order-desk-wave", "Order admin wave",
        "Ops WMS wave from order admin.",
        ("create_wave",), ("order admin wave",))
    add("portal", "order-admin-portal", "order-desk-ndr", "Order admin NDR",
        "Ops NDR from order admin.",
        ("ndr_action",), ("order admin ndr",))
    add("portal", "billing-admin-portal", "finance-gst", "Billing admin GST",
        "Finance GST compute from billing admin.",
        ("compute_gst",), ("billing admin gst",))
    add("portal", "billing-admin-portal", "finance-tcs", "Billing admin TCS",
        "Finance TCS from billing admin.",
        ("compute_tcs_194o",), ("billing admin tcs",))
    add("portal", "billing-admin-portal", "finance-ledger", "Billing admin ledger",
        "Finance journal from billing admin.",
        ("post_journal",), ("billing admin ledger",))
    add("portal", "crm-admin-portal", "crm-desk-otp", "CRM admin OTP",
        "Assisted OTP from CRM admin.",
        ("otp_start",), ("crm admin otp",))
    add("portal", "crm-admin-portal", "crm-desk-ticket", "CRM admin ticket",
        "Assisted ticket from CRM admin.",
        ("create_ticket",), ("crm admin ticket",))
    add("portal", "crm-admin-portal", "crm-desk-accounts", "CRM admin accounts",
        "Account tree from CRM admin.",
        ("account_tree",), ("crm admin tree",))
    add("portal", "crm-admin-portal", "crm-desk-dpdp", "CRM admin DPDP",
        "Consent capture from CRM admin.",
        ("record_consent",), ("crm admin dpdp",))

    # --- cross-app journeys (playbooks) ---
    add(
        "journey",
        "*",
        "checkout",
        "Journey: checkout",
        "Pincode, catalog, ATP, GST, saga, BharatQR across OMS + billing + platform.",
        (
            "pincode-master-service.serviceability",
            "product-service.list_products",
            "cart-service.add_cart_item",
            "atp-inventory-service.lock_stock",
            "gst-tax-engine.compute_gst",
            "order-orchestrator.place_order",
            "payment-gateway-service.create_bharat_qr",
            "suite.recommend_skus",
            "suite.get_order",
        ),
        ("checkout", "place order", "full checkout"),
        "checkout-delhi-upi",
        "journey",
    )
    add(
        "journey", "*", "tax", "Journey: tax desk",
        "GST + e-way + TCS 194O across billing engines.",
        ("gst-tax-engine.compute_gst", "gst-tax-engine.eway_bill", "tcs-tds-compliance-engine.compute_tcs_194o"),
        ("tax desk", "gst journey"),
        "gst-interstate-eway",
        "journey",
    )
    add(
        "journey", "*", "merchandising", "Journey: merchandising",
        "Catalog plus OMS affinity ranking.",
        ("product-service.list_products", "suite.recommend_skus", "offer-promotion-service.create_offer"),
        ("merchandising journey",),
        "merchandising-upsell",
        "journey",
    )
    add(
        "journey", "*", "fulfillment", "Journey: fulfillment",
        "ATP lock, WMS wave, NDR.",
        ("atp-inventory-service.lock_stock", "wms-fulfillment-service.create_wave", "ndr-returns-rma-service.ndr_action"),
        ("fulfillment journey",),
        "fulfillment-atp-wave",
        "journey",
    )
    add(
        "journey", "*", "billing", "Journey: billing",
        "QR, GST invoice, dunning.",
        (
            "payment-gateway-service.create_bharat_qr",
            "invoice-service.issue_invoice",
            "dunning-service.dunning_schedule",
            "gst-tax-engine.compute_gst",
        ),
        ("billing journey", "collections journey"),
        "billing-invoice-dunning",
        "journey",
    )
    add(
        "journey", "*", "crm", "Journey: CRM 360",
        "OTP, DPDP, ticket, loyalty, abandonment.",
        (
            "customer-360-service.otp_start",
            "customer-360-service.otp_verify",
            "customer-360-service.upsert_profile",
            "support-ticket-service.create_ticket",
            "loyalty-rewards-service.get_loyalty",
            "cart-abandonment-service.mark_abandoned",
            "dpdp-compliance-service.record_consent",
        ),
        ("crm journey", "customer 360 journey"),
        "crm-otp-ticket-loyalty",
        "journey",
    )

    catalog = {row.key: row for row in rows}
    # Short aliases so existing scenarios keep agent: checkout
    for row in rows:
        if row.kind == "journey":
            catalog[row.slug] = row
    return catalog


AGENTS: dict[str, AgentSpec] = _build()

APPLICATIONS = (
    "api-gateway",
    "search-solr-indexer",
    "pincode-master-service",
    "kafka-dlq-manager",
    "mca-audit-trail-service",
    "notification-service",
    "product-service",
    "variant-matrix-service",
    "serial-imei-tracking-service",
    "b2b-tiered-catalog-service",
    "component-bundle-service",
    "cpq-rule-engine",
    "dynamic-schema-engine",
    "offer-promotion-service",
    "temporal-activation-service",
    "media-dam-service",
    "bulk-catalog-import-service",
    "catalog-sync-publisher",
    "cart-service",
    "checkout-service",
    "order-orchestrator",
    "dynamic-price-engine",
    "atp-inventory-service",
    "wms-fulfillment-service",
    "ondc-seller-gateway",
    "carrier-logistics-service",
    "bopis-pickup-service",
    "ndr-returns-rma-service",
    "catalog-consumer-service",
    "gst-tax-engine",
    "tcs-tds-compliance-engine",
    "price-book-service",
    "subscription-emi-service",
    "payment-gateway-service",
    "payment-gateway-plugins",
    "cod-remittance-reconcile-service",
    "webhook-reconciliation-service",
    "invoice-service",
    "general-ledger-service",
    "dunning-service",
    "customer-360-service",
    "assisted-sales-service",
    "account-hierarchy-service",
    "contact-address-service",
    "support-ticket-service",
    "loyalty-rewards-service",
    "cart-abandonment-service",
    "dpdp-compliance-service",
    "ecommerce-storefront-portal",
    "master-admin-portal",
    "catalog-admin-studio",
    "order-admin-portal",
    "billing-admin-portal",
    "crm-admin-portal",
)


def unique_agents() -> list[AgentSpec]:
    seen: set[str] = set()
    ordered: list[AgentSpec] = []
    for spec in AGENTS.values():
        if spec.key in seen:
            continue
        seen.add(spec.key)
        ordered.append(spec)
    return ordered
