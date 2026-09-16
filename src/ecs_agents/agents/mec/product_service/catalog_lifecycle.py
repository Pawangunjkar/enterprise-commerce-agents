"""Product lifecycle LangGraph agent.

Domain `mec` / application `product-service`.
Create and activate SKUs (draft to live).
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist
from ecs_agents.enrichment import playbook_prompt

SPEC = specialist(
    domain="mec",
    application="product-service",
    slug="catalog-lifecycle",
    title="Product lifecycle",
    mission="Create, activate, IMEI-ingest, and verify SKUs in catalog and search.",
    tools=(
        "product-service.create_product",
        "product-service.activate_product",
        "product-service.list_products",
        "serial-imei-tracking-service.ingest_imei",
        "search-solr-indexer.search_products",
    ),
    keywords=("create product", "activate sku", "product lifecycle", "catalog onboarding"),
    scenario="mec-catalog-lifecycle",
)


class CatalogLifecycleAgent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You onboard SKUs for Indian retail: create_product with HSN, activate_product using "
        "the returned product id, ingest_imei for handsets, then list_products and search_products "
        "to confirm live catalog. "
        + playbook_prompt("mec-catalog-lifecycle")
    )


AGENT = CatalogLifecycleAgent()
