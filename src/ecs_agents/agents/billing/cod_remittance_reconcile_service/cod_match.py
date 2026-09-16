"""COD remittance LangGraph agent.

Domain `billing` / application `cod-remittance-reconcile-service`.
Match COD remittance vs carrier and bank amounts.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='cod-remittance-reconcile-service',
    slug='cod-match',
    title='COD remittance',
    mission='Match COD remittance vs carrier and bank amounts.',
    tools=('cod-remittance-reconcile-service.match_cod',),
    keywords=('cod remittance', 'cod match'),
)


class CodMatchAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `cod-remittance-reconcile-service`. Match COD remittance vs carrier and bank amounts. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CodMatchAgent()
