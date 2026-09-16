"""Catalog sync ops LangGraph agent.

Domain `mec` / application `catalog-sync-publisher`.
Outbound catalog sync publisher probe.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='catalog-sync-publisher',
    slug='catalog-sync-ops',
    title='Catalog sync ops',
    mission='Outbound catalog sync publisher probe.',
    tools=('catalog-sync-publisher.health',),
    keywords=('catalog sync', 'debezium'),
)


class CatalogSyncOpsAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `catalog-sync-publisher`. Outbound catalog sync publisher probe. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CatalogSyncOpsAgent()
