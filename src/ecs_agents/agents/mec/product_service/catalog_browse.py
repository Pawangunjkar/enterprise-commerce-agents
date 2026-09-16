"""Product browse LangGraph agent.

Domain `mec` / application `product-service`.
List and fetch live SKUs from product-service.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='product-service',
    slug='catalog-browse',
    title='Product browse',
    mission='List and fetch live SKUs from product-service.',
    tools=('product-service.list_products', 'product-service.get_product'),
    keywords=('list products', 'get product', 'sku browse'),
)


class CatalogBrowseAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `product-service`. List and fetch live SKUs from product-service. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CatalogBrowseAgent()
