"""Serviceability and EDD LangGraph agent.

Domain `platform` / application `pincode-master-service`.
Origin vs destination serviceability, ODA, EDD.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='pincode-master-service',
    slug='serviceability',
    title='Serviceability and EDD',
    mission='Origin vs destination serviceability, ODA, EDD.',
    tools=('pincode-master-service.serviceability',),
    keywords=('serviceability', 'edd', 'oda'),
)


class ServiceabilityAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `pincode-master-service`. Origin vs destination serviceability, ODA, EDD. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = ServiceabilityAgent()
