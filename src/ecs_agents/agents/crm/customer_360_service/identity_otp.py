"""Customer OTP LangGraph agent.

Domain `crm` / application `customer-360-service`.
Start and verify mobile OTP (live CRM, not FAQ).
"""

from ecs_agents.agents.base import CommerceAgent
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


class IdentityOtpAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `customer-360-service`. Start and verify mobile OTP (live CRM, not FAQ). Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = IdentityOtpAgent()
