"""Order admin place LangGraph agent.

Domain `portal` / application `order-admin-portal`.
Ops place-order from order admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='order-admin-portal',
    slug='order-desk-place',
    title='Order admin place',
    mission='Ops place-order from order admin.',
    tools=('order-admin-portal.place_order',),
    keywords=('order admin', 'ops place order'),
)


class OrderDeskPlaceAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `order-admin-portal`. Ops place-order from order admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = OrderDeskPlaceAgent()
