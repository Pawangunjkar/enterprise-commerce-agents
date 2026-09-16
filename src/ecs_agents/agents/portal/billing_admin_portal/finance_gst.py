"""Billing admin GST LangGraph agent.

Domain `portal` / application `billing-admin-portal`.
Finance GST compute from billing admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='billing-admin-portal',
    slug='finance-gst',
    title='Billing admin GST',
    mission='Finance GST compute from billing admin.',
    tools=('billing-admin-portal.compute_gst',),
    keywords=('billing admin gst',),
)


class FinanceGstAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `billing-admin-portal`. Finance GST compute from billing admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = FinanceGstAgent()
