"""ATP lock LangGraph agent.

Domain `oms` / application `atp-inventory-service`.
Lock available-to-promise stock in a warehouse.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='atp-inventory-service',
    slug='atp-lock',
    title='ATP lock',
    mission='Lock available-to-promise stock in a warehouse.',
    tools=('atp-inventory-service.lock_stock',),
    keywords=('atp', 'lock stock', 'inventory lock'),
)


class AtpLockAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `atp-inventory-service`. Lock available-to-promise stock in a warehouse. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = AtpLockAgent()
