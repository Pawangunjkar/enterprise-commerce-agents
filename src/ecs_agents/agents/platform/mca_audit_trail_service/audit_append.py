"""MCA audit append LangGraph agent.

Domain `platform` / application `mca-audit-trail-service`.
Write an MCA-style audit event.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='mca-audit-trail-service',
    slug='audit-append',
    title='MCA audit append',
    mission='Write an MCA-style audit event.',
    tools=('mca-audit-trail-service.append_audit',),
    keywords=('append audit', 'audit write'),
)


class AuditAppendAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `mca-audit-trail-service`. Write an MCA-style audit event. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = AuditAppendAgent()
