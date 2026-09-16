"""CRM admin accounts LangGraph agent.

Domain `portal` / application `crm-admin-portal`.
Account tree from CRM admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='crm-admin-portal',
    slug='crm-desk-accounts',
    title='CRM admin accounts',
    mission='Account tree from CRM admin.',
    tools=('crm-admin-portal.account_tree',),
    keywords=('crm admin tree',),
)


class CrmDeskAccountsAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `crm-admin-portal`. Account tree from CRM admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CrmDeskAccountsAgent()
