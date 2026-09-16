"""ONDC discovery LangGraph agent.

Domain `oms` / application `ondc-seller-gateway`.
Beckn search/select/init on the seller gateway.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='ondc-seller-gateway',
    slug='ondc-discovery',
    title='ONDC discovery',
    mission='Beckn search/select/init on the seller gateway.',
    tools=('ondc-seller-gateway.beckn_search', 'ondc-seller-gateway.beckn_select', 'ondc-seller-gateway.beckn_init'),
    keywords=('ondc search', 'beckn search', 'beckn select'),
)


class OndcDiscoveryAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `ondc-seller-gateway`. Beckn search/select/init on the seller gateway. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = OndcDiscoveryAgent()
