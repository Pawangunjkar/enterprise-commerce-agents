"""Journey: CRM 360 LangGraph agent.

Domain `journey` / application `*`.
OTP, DPDP, ticket, loyalty, abandonment.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import journey
from ecs_agents.enrichment import playbook_prompt

SPEC = journey(
    slug="crm",
    title="Journey: CRM 360",
    mission="OTP identity, KYC upsert, DPDP consent, ticket, loyalty, abandonment.",
    tools=(
        "customer-360-service.otp_start",
        "customer-360-service.otp_verify",
        "customer-360-service.upsert_profile",
        "customer-360-service.get_profile",
        "support-ticket-service.create_ticket",
        "loyalty-rewards-service.get_loyalty",
        "cart-abandonment-service.mark_abandoned",
        "dpdp-compliance-service.record_consent",
        "account-hierarchy-service.account_tree",
        "contact-address-service.autofill_address",
        "assisted-sales-service.create_paylink",
    ),
    keywords=("crm journey", "customer 360 journey", "otp ticket loyalty", "assisted sales paylink"),
    scenario="crm-otp-ticket-loyalty",
)


class CrmAgent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You own the CRM assisted-sales journey across Customer 360, DPDP, tickets, and loyalty. "
        "Mobile number is the customer id. Run enrichment before the final action when the user "
        "asks for the full flow. "
        + playbook_prompt("crm-full")
        + "\n"
        + playbook_prompt("crm-assisted-sales")
    )


AGENT = CrmAgent()
