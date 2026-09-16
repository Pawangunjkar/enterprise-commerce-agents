"""Gateway health LangGraph agent.

Domain `platform` / application `api-gateway`.
Probe gateway liveness before other MCP calls.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='api-gateway',
    slug='health',
    title='Gateway health',
    mission='Probe gateway liveness before other MCP calls.',
    tools=('api-gateway.health',),
    keywords=('gateway health', 'gateway up'),
)


class HealthAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `api-gateway`. Probe gateway liveness before other MCP calls. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = HealthAgent()
