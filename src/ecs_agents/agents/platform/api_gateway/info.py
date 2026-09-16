"""Gateway info LangGraph agent.

Domain `platform` / application `api-gateway`.
Read gateway build/info from the edge.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='api-gateway',
    slug='info',
    title='Gateway info',
    mission='Read gateway build/info from the edge.',
    tools=('api-gateway.info',),
    keywords=('gateway info', 'gateway version'),
)


class InfoAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `api-gateway`. Read gateway build/info from the edge. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = InfoAgent()
