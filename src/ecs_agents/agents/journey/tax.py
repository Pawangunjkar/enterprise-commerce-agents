"""Journey: tax desk LangGraph agent.

Domain `journey` / application `*`.
GST + e-way + TCS 194O across billing engines.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import journey

SPEC = journey(
    slug='tax',
    title='Journey: tax desk',
    mission='GST + e-way + TCS 194O across billing engines.',
    tools=('gst-tax-engine.compute_gst', 'gst-tax-engine.eway_bill', 'tcs-tds-compliance-engine.compute_tcs_194o'),
    keywords=('tax desk', 'gst journey'),
    scenario='gst-interstate-eway',
)


class TaxAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You own this cross-application journey. Call MCP tools in business order when the user wants the full flow: gst-tax-engine.compute_gst -> gst-tax-engine.eway_bill -> tcs-tds-compliance-engine.compute_tcs_194o. Stop and report if any step errors. GST + e-way + TCS 194O across billing engines.'


AGENT = TaxAgent()
