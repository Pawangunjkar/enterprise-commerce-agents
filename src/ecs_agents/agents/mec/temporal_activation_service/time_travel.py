"""Temporal catalog LangGraph agent.

Domain `mec` / application `temporal-activation-service`.
Read catalog as-of a timestamp.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='temporal-activation-service',
    slug='time-travel',
    title='Temporal catalog',
    mission='Read catalog as-of a timestamp.',
    tools=('temporal-activation-service.time_travel',),
    keywords=('time travel', 'as-of', 'temporal'),
)


class TimeTravelAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `temporal-activation-service`. Read catalog as-of a timestamp. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = TimeTravelAgent()
