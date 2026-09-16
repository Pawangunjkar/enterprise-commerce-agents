"""BOPIS reserve LangGraph agent.

Domain `oms` / application `bopis-pickup-service`.
Reserve buy-online-pickup-in-store inventory.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='bopis-pickup-service',
    slug='bopis-reserve',
    title='BOPIS reserve',
    mission='Reserve buy-online-pickup-in-store inventory.',
    tools=('bopis-pickup-service.reserve_pickup',),
    keywords=('bopis', 'pickup reserve', 'click collect'),
)


class BopisReserveAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `bopis-pickup-service`. Reserve buy-online-pickup-in-store inventory. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = BopisReserveAgent()
