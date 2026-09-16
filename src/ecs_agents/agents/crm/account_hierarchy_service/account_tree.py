"""B2B account tree LangGraph agent.

Domain `crm` / application `account-hierarchy-service`.
Read dealer/distributor account hierarchy.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='account-hierarchy-service',
    slug='account-tree',
    title='B2B account tree',
    mission='Read dealer/distributor account hierarchy.',
    tools=('account-hierarchy-service.account_tree',),
    keywords=('account tree', 'b2b hierarchy'),
)


class AccountTreeAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `account-hierarchy-service`. Read dealer/distributor account hierarchy. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = AccountTreeAgent()
