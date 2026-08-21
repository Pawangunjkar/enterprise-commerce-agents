"""Journey: CRM 360.

Domain journey / application *.
OTP, DPDP, ticket, loyalty, abandonment.
"""

from ecs_agents.agents.spec import journey

SPEC = journey(
    slug='crm',
    title='Journey: CRM 360',
    mission='OTP, DPDP, ticket, loyalty, abandonment.',
    tools=('customer-360-service.otp_start', 'customer-360-service.otp_verify', 'customer-360-service.upsert_profile', 'support-ticket-service.create_ticket', 'loyalty-rewards-service.get_loyalty', 'cart-abandonment-service.mark_abandoned', 'dpdp-compliance-service.record_consent'),
    keywords=('crm journey', 'customer 360 journey'),
    scenario='crm-otp-ticket-loyalty',
)
