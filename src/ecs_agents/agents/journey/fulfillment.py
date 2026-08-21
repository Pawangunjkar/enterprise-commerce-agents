"""Journey: fulfillment.

Domain journey / application *.
ATP lock, WMS wave, NDR.
"""

from ecs_agents.agents.spec import journey

SPEC = journey(
    slug='fulfillment',
    title='Journey: fulfillment',
    mission='ATP lock, WMS wave, NDR.',
    tools=('atp-inventory-service.lock_stock', 'wms-fulfillment-service.create_wave', 'ndr-returns-rma-service.ndr_action'),
    keywords=('fulfillment journey',),
    scenario='fulfillment-atp-wave',
)
