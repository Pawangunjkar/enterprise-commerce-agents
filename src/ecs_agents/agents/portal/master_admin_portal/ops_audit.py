"""Master admin audit LangGraph agent.

Domain `portal` / application `master-admin-portal`.
Ops audit query from master admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='master-admin-portal',
    slug='ops-audit',
    title='Master admin audit',
    mission='Ops audit query from master admin.',
    tools=('master-admin-portal.list_audit',),
    keywords=('master admin audit',),
)


class OpsAuditAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `master-admin-portal`. Ops audit query from master admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = OpsAuditAgent()
