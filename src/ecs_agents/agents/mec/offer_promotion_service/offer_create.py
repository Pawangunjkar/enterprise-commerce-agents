"""Offer authoring LangGraph agent.

Domain `mec` / application `offer-promotion-service`.
Create a live promotion/offer.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist
from ecs_agents.enrichment import playbook_prompt

SPEC = specialist(
    domain="mec",
    application="offer-promotion-service",
    slug="offer-create",
    title="Offer authoring",
    mission="Schema validate → CPQ → create offer → temporal activation preview.",
    tools=(
        "dynamic-schema-engine.validate_schema",
        "cpq-rule-engine.evaluate_cpq",
        "offer-promotion-service.create_offer",
        "temporal-activation-service.time_travel",
    ),
    keywords=("create offer", "promotion", "festival offer", "offer promo"),
    scenario="mec-offer-promo",
)


class OfferCreateAgent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You author MEC promotional offers for Indian retail. Validate schema, run evaluate_cpq, "
        "create_offer with offerCode and sku, then time_travel to preview activation. "
        + playbook_prompt("mec-offer-promo")
    )


AGENT = OfferCreateAgent()
