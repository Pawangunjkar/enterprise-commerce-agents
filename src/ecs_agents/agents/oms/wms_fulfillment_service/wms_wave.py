"""WMS pick wave LangGraph agent.

Domain `oms` / application `wms-fulfillment-service`.
Release a warehouse pick wave.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='wms-fulfillment-service',
    slug='wms-wave',
    title='WMS pick wave',
    mission='Release a warehouse pick wave.',
    tools=('wms-fulfillment-service.create_wave',),
    keywords=('wms', 'pick wave', 'warehouse wave'),
)


class WmsWaveAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `wms-fulfillment-service`. Release a warehouse pick wave. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = WmsWaveAgent()
