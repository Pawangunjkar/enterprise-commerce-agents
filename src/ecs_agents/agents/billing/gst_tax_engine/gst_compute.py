"""GST compute LangGraph agent.

Domain `billing` / application `gst-tax-engine`.
Intra CGST+SGST vs inter IGST on a taxable value.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='gst-tax-engine',
    slug='gst-compute',
    title='GST compute',
    mission='Intra CGST+SGST vs inter IGST on a taxable value.',
    tools=('gst-tax-engine.compute_gst',),
    keywords=('compute gst', 'cgst', 'sgst', 'igst', 'gst slab'),
    scenario='gst-interstate-eway',
)


class GstComputeAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `gst-tax-engine`. Intra CGST+SGST vs inter IGST on a taxable value. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = GstComputeAgent()
