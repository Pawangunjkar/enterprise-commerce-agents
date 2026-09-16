"""Order admin NDR LangGraph agent.

Domain `portal` / application `order-admin-portal`.
Ops NDR from order admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='order-admin-portal',
    slug='order-desk-ndr',
    title='Order admin NDR',
    mission='Ops NDR from order admin.',
    tools=('order-admin-portal.ndr_action',),
    keywords=('order admin ndr',),
)


class OrderDeskNdrAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `order-admin-portal`. Ops NDR from order admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = OrderDeskNdrAgent()
