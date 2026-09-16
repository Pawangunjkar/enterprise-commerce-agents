"""CRM admin OTP LangGraph agent.

Domain `portal` / application `crm-admin-portal`.
Assisted OTP from CRM admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='crm-admin-portal',
    slug='crm-desk-otp',
    title='CRM admin OTP',
    mission='Assisted OTP from CRM admin.',
    tools=('crm-admin-portal.otp_start',),
    keywords=('crm admin otp',),
)


class CrmDeskOtpAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `crm-admin-portal`. Assisted OTP from CRM admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CrmDeskOtpAgent()
