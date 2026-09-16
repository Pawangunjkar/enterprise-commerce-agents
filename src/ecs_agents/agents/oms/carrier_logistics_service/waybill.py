"""Waybill create LangGraph agent.

Domain `oms` / application `carrier-logistics-service`.
Create a carrier waybill/AWB.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='carrier-logistics-service',
    slug='waybill',
    title='Waybill create',
    mission='Create a carrier waybill/AWB.',
    tools=('carrier-logistics-service.create_waybill',),
    keywords=('waybill', 'awb create', 'shipment'),
)


class WaybillAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `carrier-logistics-service`. Create a carrier waybill/AWB. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = WaybillAgent()
