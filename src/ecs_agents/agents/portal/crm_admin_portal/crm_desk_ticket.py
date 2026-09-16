"""CRM admin ticket LangGraph agent.

Domain `portal` / application `crm-admin-portal`.
Assisted ticket from CRM admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='crm-admin-portal',
    slug='crm-desk-ticket',
    title='CRM admin ticket',
    mission='Assisted ticket from CRM admin.',
    tools=('crm-admin-portal.create_ticket',),
    keywords=('crm admin ticket',),
)


class CrmDeskTicketAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `crm-admin-portal`. Assisted ticket from CRM admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CrmDeskTicketAgent()
