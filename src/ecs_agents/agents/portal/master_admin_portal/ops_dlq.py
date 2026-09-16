"""Master admin DLQ LangGraph agent.

Domain `portal` / application `master-admin-portal`.
Ops DLQ from master admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='master-admin-portal',
    slug='ops-dlq',
    title='Master admin DLQ',
    mission='Ops DLQ from master admin.',
    tools=('master-admin-portal.list_dlq', 'master-admin-portal.replay_dlq'),
    keywords=('master admin dlq',),
)


class OpsDlqAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `master-admin-portal`. Ops DLQ from master admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = OpsDlqAgent()
