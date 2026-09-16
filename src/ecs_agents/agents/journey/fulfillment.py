"""Journey: fulfillment LangGraph agent.

Domain `journey` / application `*`.
Order load, ATP lock, WMS wave, carrier waybill, NDR.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import journey
from ecs_agents.enrichment import playbook_prompt

SPEC = journey(
    slug="fulfillment",
    title="Journey: fulfillment",
    mission="Order → ATP lock → WMS wave → carrier waybill → NDR.",
    tools=(
        "suite.get_order",
        "atp-inventory-service.lock_stock",
        "wms-fulfillment-service.create_wave",
        "carrier-logistics-service.check_serviceability",
        "carrier-logistics-service.create_waybill",
        "ndr-returns-rma-service.ndr_action",
    ),
    keywords=("fulfillment journey", "order to fulfillment", "wms wave"),
    scenario="oms-order-to-fulfillment",
)


class FulfillmentAgent(CommerceAgent):
    spec = SPEC
    instructions = (
        "You own post-checkout fulfillment: load the order, lock ATP, release a WMS pick wave, "
        "book carrier serviceability and waybill, then handle NDR if needed. "
        + playbook_prompt("oms-fulfillment")
    )


AGENT = FulfillmentAgent()
