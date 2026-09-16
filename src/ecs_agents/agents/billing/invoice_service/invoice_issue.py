"""GST invoice LangGraph agent.

Domain `billing` / application `invoice-service`.
Issue and persist a GST tax invoice.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='invoice-service',
    slug='invoice-issue',
    title='GST invoice',
    mission='Issue and persist a GST tax invoice.',
    tools=('invoice-service.issue_invoice',),
    keywords=('issue invoice', 'tax invoice', 'gst invoice'),
    scenario='billing-invoice-dunning',
)


class InvoiceIssueAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `invoice-service`. Issue and persist a GST tax invoice. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = InvoiceIssueAgent()
