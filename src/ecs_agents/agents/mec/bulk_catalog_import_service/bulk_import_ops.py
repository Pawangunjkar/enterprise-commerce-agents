"""Bulk import ops LangGraph agent.

Domain `mec` / application `bulk-catalog-import-service`.
Bulk catalog import worker probe.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='bulk-catalog-import-service',
    slug='bulk-import-ops',
    title='Bulk import ops',
    mission='Bulk catalog import worker probe.',
    tools=('bulk-catalog-import-service.health',),
    keywords=('bulk import', 'catalog import'),
)


class BulkImportOpsAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `bulk-catalog-import-service`. Bulk catalog import worker probe. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = BulkImportOpsAgent()
