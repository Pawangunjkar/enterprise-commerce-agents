"""Solr faceted search LangGraph agent.

Domain `platform` / application `search-solr-indexer`.
Live product search with brand/RAM/price facets.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='search-solr-indexer',
    slug='faceted-search',
    title='Solr faceted search',
    mission='Live product search with brand/RAM/price facets.',
    tools=('search-solr-indexer.search_products',),
    keywords=('solr', 'faceted search', 'search products'),
)


class FacetedSearchAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `search-solr-indexer`. Live product search with brand/RAM/price facets. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = FacetedSearchAgent()
