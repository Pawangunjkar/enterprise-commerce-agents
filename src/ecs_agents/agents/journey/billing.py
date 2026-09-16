"""Journey: billing LangGraph agent.

Domain `journey` / application `*`.
QR, GST invoice, dunning.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import journey

SPEC = journey(
    slug='billing',
    title='Journey: billing',
    mission='QR, GST invoice, dunning.',
    tools=('payment-gateway-service.create_bharat_qr', 'invoice-service.issue_invoice', 'dunning-service.dunning_schedule', 'gst-tax-engine.compute_gst'),
    keywords=('billing journey', 'collections journey'),
    scenario='billing-invoice-dunning',
)


class BillingAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You own this cross-application journey. Call MCP tools in business order when the user wants the full flow: payment-gateway-service.create_bharat_qr -> invoice-service.issue_invoice -> dunning-service.dunning_schedule -> gst-tax-engine.compute_gst. Stop and report if any step errors. QR, GST invoice, dunning.'


AGENT = BillingAgent()
