"""Billing admin ledger LangGraph agent.

Domain `portal` / application `billing-admin-portal`.
Finance journal from billing admin.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='billing-admin-portal',
    slug='finance-ledger',
    title='Billing admin ledger',
    mission='Finance journal from billing admin.',
    tools=('billing-admin-portal.post_journal',),
    keywords=('billing admin ledger',),
)


class FinanceLedgerAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `billing-admin-portal`. Finance journal from billing admin. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = FinanceLedgerAgent()
