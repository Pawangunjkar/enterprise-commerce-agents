"""MCA audit query LangGraph agent.

Domain `platform` / application `mca-audit-trail-service`.
Page audit events by resource type.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='mca-audit-trail-service',
    slug='audit-query',
    title='MCA audit query',
    mission='Page audit events by resource type.',
    tools=('mca-audit-trail-service.list_audit',),
    keywords=('list audit', 'audit trail'),
)


class AuditQueryAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `mca-audit-trail-service`. Page audit events by resource type. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = AuditQueryAgent()
