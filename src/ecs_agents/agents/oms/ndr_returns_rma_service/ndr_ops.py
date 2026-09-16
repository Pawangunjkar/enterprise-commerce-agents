"""NDR / RMA LangGraph agent.

Domain `oms` / application `ndr-returns-rma-service`.
Take NDR action (reattempt, rto) on an AWB.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='ndr-returns-rma-service',
    slug='ndr-ops',
    title='NDR / RMA',
    mission='Take NDR action (reattempt, rto) on an AWB.',
    tools=('ndr-returns-rma-service.ndr_action',),
    keywords=('ndr', 'rma', 'reattempt', 'rto'),
    scenario='fulfillment-atp-wave',
)


class NdrOpsAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `ndr-returns-rma-service`. Take NDR action (reattempt, rto) on an AWB. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = NdrOpsAgent()
