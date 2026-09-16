"""Journey: MEC catalog LangGraph agent.

Domain `journey` / application `*`.
Catalog lifecycle, B2B tier quote, CPQ, and offer authoring across MEC + CRM hierarchy.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import journey
from ecs_agents.enrichment import playbook_prompt

SPEC = journey(
    slug="mec-catalog",
    title="Journey: MEC catalog",
    mission="Create/activate SKUs, IMEI ingest, B2B tier quote, CPQ bundle, and promotional offers.",
    tools=(
        "product-service.create_product",
        "product-service.activate_product",
        "product-service.list_products",
        "serial-imei-tracking-service.ingest_imei",
        "search-solr-indexer.search_products",
        "account-hierarchy-service.account_tree",
        "b2b-tiered-catalog-service.b2b_quote",
        "component-bundle-service.price_bundle",
        "cpq-rule-engine.evaluate_cpq",
        "dynamic-schema-engine.validate_schema",
        "offer-promotion-service.create_offer",
        "temporal-activation-service.time_travel",
    ),
    keywords=("mec journey", "catalog lifecycle", "b2b quote journey", "cpq offer"),
    scenario="mec-catalog-lifecycle",
)


class MecCatalogAgent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You own Master Enterprise Catalog (MEC) end-to-end flows across product, IMEI, B2B, CPQ, and offers. "
        "For catalog onboarding: create_product → activate_product → ingest_imei → list_products → search_products. "
        "For B2B: account_tree → b2b_quote → price_bundle → evaluate_cpq. "
        "For promotions: validate_schema → evaluate_cpq → create_offer → time_travel preview. "
        + playbook_prompt("mec-catalog-lifecycle")
        + "\n"
        + playbook_prompt("mec-b2b-quote")
        + "\n"
        + playbook_prompt("mec-offer-promo")
    )


AGENT = MecCatalogAgent()
