"""Shared agent contract. Each operator lives in its own module under ecs_agents.agents."""

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
    kind: str = "specialist"

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

    @property
    def module_path(self) -> str:
        if self.kind == "journey":
            return f"ecs_agents.agents.journey.{_ident(self.slug)}"
        return f"ecs_agents.agents.{self.domain}.{_ident(self.application)}.{_ident(self.slug)}"


def mcp_module(server: str) -> str:
    return "ecs_mcps." + server.replace("-", "_")


def _ident(name: str) -> str:
    return name.replace("-", "_").replace("*", "squads")


def _qualify(app: str, tools: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(tool if "." in tool else f"{app}.{tool}" for tool in tools)


def specialist(
    *,
    domain: str,
    application: str,
    slug: str,
    title: str,
    mission: str,
    tools: tuple[str, ...],
    keywords: tuple[str, ...],
    scenario: str = "",
) -> AgentSpec:
    return AgentSpec(
        key=f"{domain}.{application}.{slug}",
        domain=domain,
        application=application,
        slug=slug,
        title=title,
        mission=mission,
        tools=_qualify(application, tools),
        keywords=keywords,
        default_scenario=scenario,
        kind="specialist",
    )


def journey(
    *,
    slug: str,
    title: str,
    mission: str,
    tools: tuple[str, ...],
    keywords: tuple[str, ...],
    scenario: str = "",
) -> AgentSpec:
    return AgentSpec(
        key=f"journey.*.{slug}",
        domain="journey",
        application="*",
        slug=slug,
        title=title,
        mission=mission,
        tools=tools,
        keywords=keywords,
        default_scenario=scenario,
        kind="journey",
    )
