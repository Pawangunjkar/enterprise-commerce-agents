"""B2B tier quote LangGraph agent.

Domain `mec` / application `b2b-tiered-catalog-service`.
Quote a dealer/distributor tier price.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist
from ecs_agents.enrichment import playbook_prompt

SPEC = specialist(
    domain="mec",
    application="b2b-tiered-catalog-service",
    slug="b2b-quote",
    title="B2B tier quote",
    mission="Account tree → B2B tier quote → bundle price → CPQ evaluation.",
    tools=(
        "account-hierarchy-service.account_tree",
        "b2b-tiered-catalog-service.b2b_quote",
        "component-bundle-service.price_bundle",
        "cpq-rule-engine.evaluate_cpq",
    ),
    keywords=("b2b", "dealer price", "tier quote", "distributor quote"),
    scenario="mec-b2b-tier-quote",
)


class B2bQuoteAgent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You quote B2B tier prices for Indian dealer/distributor accounts. Load account_tree first, "
        "then b2b_quote with accountId and sku from the tree, price_bundle for kit SKUs, and "
        "evaluate_cpq for rule validation. "
        + playbook_prompt("mec-b2b-quote")
    )


AGENT = B2bQuoteAgent()
