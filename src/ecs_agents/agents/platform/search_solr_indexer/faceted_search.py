"""Solr faceted search.

Domain platform / application search-solr-indexer.
Live product search with brand/RAM/price facets.
"""

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
