"""E-way bill LangGraph agent.

Domain `billing` / application `gst-tax-engine`.
E-way bill required flag when taxable exceeds threshold.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='gst-tax-engine',
    slug='eway-bill',
    title='E-way bill',
    mission='E-way bill required flag when taxable exceeds threshold.',
    tools=('gst-tax-engine.eway_bill',),
    keywords=('e-way', 'eway', 'e-way bill', 'eway bill'),
)


class EwayBillAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `gst-tax-engine`. E-way bill required flag when taxable exceeds threshold. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = EwayBillAgent()
