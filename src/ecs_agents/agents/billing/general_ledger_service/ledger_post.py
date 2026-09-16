"""General ledger LangGraph agent.

Domain `billing` / application `general-ledger-service`.
Post a GAAP journal entry.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='general-ledger-service',
    slug='ledger-post',
    title='General ledger',
    mission='Post a GAAP journal entry.',
    tools=('general-ledger-service.post_journal',),
    keywords=('journal', 'general ledger', 'gaap'),
)


class LedgerPostAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `general-ledger-service`. Post a GAAP journal entry. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = LedgerPostAgent()
