"""Order admin wave LangGraph agent.

Domain `portal` / application `order-admin-portal`.
Ops WMS wave from order admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='order-admin-portal',
    slug='order-desk-wave',
    title='Order admin wave',
    mission='Ops WMS wave from order admin.',
    tools=('order-admin-portal.create_wave',),
    keywords=('order admin wave',),
)


class OrderDeskWaveAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `order-admin-portal`. Ops WMS wave from order admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = OrderDeskWaveAgent()
