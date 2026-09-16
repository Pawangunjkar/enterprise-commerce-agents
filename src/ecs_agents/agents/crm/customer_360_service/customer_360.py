"""Customer 360 LangGraph agent.

Domain `crm` / application `customer-360-service`.
Assemble a live identity, KYC, loyalty, tickets, and consent dossier.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist
from ecs_agents.enrichment import playbook_prompt

SPEC = specialist(
    domain="crm",
    application="customer-360-service",
    slug="customer-360",
    title="Customer 360",
    mission="Build a live Customer 360 dossier: KYC profile, OTP identity, loyalty, tickets, B2B tree, address, consent.",
    tools=(
        "customer-360-service.get_profile",
        "customer-360-service.upsert_profile",
        "customer-360-service.otp_start",
        "customer-360-service.otp_verify",
        "loyalty-rewards-service.get_loyalty",
        "support-ticket-service.create_ticket",
        "account-hierarchy-service.account_tree",
        "contact-address-service.autofill_address",
        "cart-abandonment-service.mark_abandoned",
        "dpdp-compliance-service.record_consent",
        "assisted-sales-service.create_paylink",
    ),
    keywords=(
        "customer 360",
        "360 view",
        "customer snapshot",
        "unified customer",
        "customer dossier",
        "kyc 360",
    ),
    scenario="customer-360-view",
)


class Customer360Agent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You own Customer 360 for Indian retail/B2B. Mobile number is the customer id. "
        "Call get_profile first. Then pull loyalty (customerId = mobile), account_tree, "
        "and autofill_address when a pincode is present. "
        "OTP-verify only when the user supplies an OTP (lab default is 123456). "
        "upsert_profile when they give name, PAN, or GSTIN. "
        "create_ticket / record_consent / mark_abandoned / create_paylink only when asked. "
        "Return a short dossier: identity, KYC, loyalty points/tier, hierarchy, address, open actions. "
        "Never invent PAN, GSTIN, or points — quote tool JSON. "
        + playbook_prompt("crm-full")
        + "\n"
        + playbook_prompt("crm-assisted-sales")
    )


AGENT = Customer360Agent()
