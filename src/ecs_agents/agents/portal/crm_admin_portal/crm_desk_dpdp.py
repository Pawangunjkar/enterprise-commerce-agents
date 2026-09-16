"""CRM admin DPDP LangGraph agent.

Domain `portal` / application `crm-admin-portal`.
Consent capture from CRM admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='crm-admin-portal',
    slug='crm-desk-dpdp',
    title='CRM admin DPDP',
    mission='Consent capture from CRM admin.',
    tools=('crm-admin-portal.record_consent',),
    keywords=('crm admin dpdp',),
)


class CrmDeskDpdpAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `crm-admin-portal`. Consent capture from CRM admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CrmDeskDpdpAgent()
