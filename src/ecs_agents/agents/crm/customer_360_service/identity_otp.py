"""Customer OTP.

Domain crm / application customer-360-service.
Start and verify mobile OTP (live CRM, not FAQ).
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='customer-360-service',
    slug='identity-otp',
    title='Customer OTP',
    mission='Start and verify mobile OTP (live CRM, not FAQ).',
    tools=('customer-360-service.otp_start', 'customer-360-service.otp_verify'),
    keywords=('otp', 'verify otp', 'mobile otp'),
)
