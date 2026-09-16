"""Search autocomplete LangGraph agent.

Domain `platform` / application `search-solr-indexer`.
Typeahead from the Solr products collection.
"""

from ecs_agents.agents.base import CommerceAgent
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


class AutocompleteAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `search-solr-indexer`. Typeahead from the Solr products collection. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = AutocompleteAgent()
