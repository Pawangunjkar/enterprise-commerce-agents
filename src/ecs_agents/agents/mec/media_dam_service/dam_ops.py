"""DAM ops LangGraph agent.

Domain `mec` / application `media-dam-service`.
Media/DAM service health and ops probe.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='media-dam-service',
    slug='dam-ops',
    title='DAM ops',
    mission='Media/DAM service health and ops probe.',
    tools=('media-dam-service.health',),
    keywords=('dam', 'media asset'),
)


class DamOpsAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `media-dam-service`. Media/DAM service health and ops probe. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = DamOpsAgent()
