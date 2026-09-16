"""OMS catalog consumer LangGraph agent.

Domain `oms` / application `catalog-consumer-service`.
OMS replica consumer health probe.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='catalog-consumer-service',
    slug='oms-catalog-consumer',
    title='OMS catalog consumer',
    mission='OMS replica consumer health probe.',
    tools=('catalog-consumer-service.health',),
    keywords=('catalog consumer', 'oms replica'),
)


class OmsCatalogConsumerAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `catalog-consumer-service`. OMS replica consumer health probe. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = OmsCatalogConsumerAgent()
