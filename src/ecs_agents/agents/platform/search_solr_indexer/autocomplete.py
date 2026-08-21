"""Search autocomplete.

Domain platform / application search-solr-indexer.
Typeahead from the Solr products collection.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='search-solr-indexer',
    slug='autocomplete',
    title='Search autocomplete',
    mission='Typeahead from the Solr products collection.',
    tools=('search-solr-indexer.autocomplete',),
    keywords=('autocomplete', 'typeahead'),
)
