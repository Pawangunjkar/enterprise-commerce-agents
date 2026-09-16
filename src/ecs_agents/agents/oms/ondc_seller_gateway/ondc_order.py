"""ONDC order lifecycle LangGraph agent.

Domain `oms` / application `ondc-seller-gateway`.
Beckn confirm, status, track, cancel.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='ondc-seller-gateway',
    slug='ondc-order',
    title='ONDC order lifecycle',
    mission='Beckn confirm, status, track, cancel.',
    tools=('ondc-seller-gateway.beckn_confirm', 'ondc-seller-gateway.beckn_status', 'ondc-seller-gateway.beckn_track', 'ondc-seller-gateway.beckn_cancel'),
    keywords=('ondc confirm', 'beckn track', 'beckn cancel'),
)


class OndcOrderAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `ondc-seller-gateway`. Beckn confirm, status, track, cancel. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = OndcOrderAgent()
