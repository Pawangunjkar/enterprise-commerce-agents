"""Dunning schedule LangGraph agent.

Domain `billing` / application `dunning-service`.
Read the live collections/dunning calendar.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='dunning-service',
    slug='dunning-schedule',
    title='Dunning schedule',
    mission='Read the live collections/dunning calendar.',
    tools=('dunning-service.dunning_schedule',),
    keywords=('dunning', 'collections calendar'),
)


class DunningScheduleAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `dunning-service`. Read the live collections/dunning calendar. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = DunningScheduleAgent()
