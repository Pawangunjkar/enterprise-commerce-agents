"""Pincode master lookup LangGraph agent.

Domain `platform` / application `pincode-master-service`.
Load India pincode master attributes.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='pincode-master-service',
    slug='pincode-lookup',
    title='Pincode master lookup',
    mission='Load India pincode master attributes.',
    tools=('pincode-master-service.get_pincode',),
    keywords=('pincode lookup', 'pincode master'),
)


class PincodeLookupAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `pincode-master-service`. Load India pincode master attributes. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = PincodeLookupAgent()
