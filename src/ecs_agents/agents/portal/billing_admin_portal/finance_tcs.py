"""Billing admin TCS LangGraph agent.

Domain `portal` / application `billing-admin-portal`.
Finance TCS from billing admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='billing-admin-portal',
    slug='finance-tcs',
    title='Billing admin TCS',
    mission='Finance TCS from billing admin.',
    tools=('billing-admin-portal.compute_tcs_194o',),
    keywords=('billing admin tcs',),
)


class FinanceTcsAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `billing-admin-portal`. Finance TCS from billing admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = FinanceTcsAgent()
