"""Carrier serviceability LangGraph agent.

Domain `oms` / application `carrier-logistics-service`.
Ask Delhivery/Shiprocket/BlueDart style serviceability.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='carrier-logistics-service',
    slug='carrier-serviceability',
    title='Carrier serviceability',
    mission='Ask Delhivery/Shiprocket/BlueDart style serviceability.',
    tools=('carrier-logistics-service.check_serviceability',),
    keywords=('carrier serviceability', 'delhivery', 'shiprocket'),
)


class CarrierServiceabilityAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `carrier-logistics-service`. Ask Delhivery/Shiprocket/BlueDart style serviceability. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CarrierServiceabilityAgent()
