"""Storefront search LangGraph agent.

Domain `portal` / application `ecommerce-storefront-portal`.
Buyer-facing Solr search from the storefront portal MCP.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='ecommerce-storefront-portal',
    slug='store-search',
    title='Storefront search',
    mission='Buyer-facing Solr search from the storefront portal MCP.',
    tools=('ecommerce-storefront-portal.search_store',),
    keywords=('storefront search', 'store search'),
)


class StoreSearchAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `ecommerce-storefront-portal`. Buyer-facing Solr search from the storefront portal MCP. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = StoreSearchAgent()
