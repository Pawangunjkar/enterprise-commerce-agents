"""TCS 194O LangGraph agent.

Domain `billing` / application `tcs-tds-compliance-engine`.
Section 194O TCS on e-commerce GMV.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='tcs-tds-compliance-engine',
    slug='tcs-194o',
    title='TCS 194O',
    mission='Section 194O TCS on e-commerce GMV.',
    tools=('tcs-tds-compliance-engine.compute_tcs_194o',),
    keywords=('tcs', '194o', '194-o'),
)


class Tcs194oAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `tcs-tds-compliance-engine`. Section 194O TCS on e-commerce GMV. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = Tcs194oAgent()
