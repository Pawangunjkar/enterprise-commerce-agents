"""Assisted pay-link LangGraph agent.

Domain `crm` / application `assisted-sales-service`.
Create a store-assisted payment link.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist
from ecs_agents.enrichment import playbook_prompt

SPEC = specialist(
    domain="crm",
    application="assisted-sales-service",
    slug="assisted-paylink",
    title="Assisted pay-link",
    mission="Profile + loyalty + consent enrichment, then mint assisted pay-link.",
    tools=(
        "customer-360-service.get_profile",
        "loyalty-rewards-service.get_loyalty",
        "dpdp-compliance-service.record_consent",
        "assisted-sales-service.create_paylink",
    ),
    keywords=("paylink", "assisted sales", "store associate", "whatsapp pay link"),
    scenario="crm-assisted-sales-paylink",
)


class AssistedPaylinkAgent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You are the assisted-sales desk operator. Load get_profile and get_loyalty before "
        "create_paylink. Record record_consent when checkout involves personal data. "
        + playbook_prompt("crm-assisted-sales")
    )


AGENT = AssistedPaylinkAgent()
