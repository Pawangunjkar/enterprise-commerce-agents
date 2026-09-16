from ecs_agents.agents.spec import APPLICATIONS
from ecs_agents.catalog import unique_agents
from ecs_agents.registry import route_agent
from ecs_agents.scenarios import resolve_value


def test_routes_eway_to_gst_tax_engine() -> None:
    key = route_agent("Need e-way bill for MH shipment")
    assert key == "billing.gst-tax-engine.eway-bill"


def test_routes_recommendations_to_oms_merchandising() -> None:
    key = route_agent("Show cross-sell and upsell for this SKU")
    assert key == "oms.order-orchestrator.merchandising"


def test_routes_ndr_to_ndr_service() -> None:
    key = route_agent("Reattempt NDR for this AWB")
    assert key == "oms.ndr-returns-rma-service.ndr-ops"


def test_routes_customer_360() -> None:
    key = route_agent("Show customer 360 for 9999999999")
    assert key == "crm.customer-360-service.customer-360"


def test_jsonpath_walks_nested_and_data_wrapper() -> None:
    ctx = {"order": {"data": {"orderId": "abc-123"}, "success": True}}
    assert resolve_value("$.order.data.orderId", ctx) == "abc-123"
    assert resolve_value("$.order.orderId", ctx) == "abc-123"


def test_jsonpath_in_args() -> None:
    ctx = {"order": {"data": {"orderId": "oid-9"}}}
    args = resolve_value({"orderId": "$.order.data.orderId", "amount": 10}, ctx)
    assert args == {"orderId": "oid-9", "amount": 10}


def test_every_application_has_at_least_one_agent() -> None:
    covered = {spec.application for spec in unique_agents() if spec.kind == "specialist"}
    missing = [app for app in APPLICATIONS if app not in covered]
    assert missing == []


def test_multi_agent_apps_have_more_than_one_specialist() -> None:
    from collections import Counter

    counts = Counter(spec.application for spec in unique_agents() if spec.kind == "specialist")
    assert counts["product-service"] >= 2
    assert counts["gst-tax-engine"] >= 2
    assert counts["order-orchestrator"] >= 2
    assert counts["payment-gateway-service"] >= 2
    assert counts["customer-360-service"] >= 3
    assert counts["ondc-seller-gateway"] >= 2


def test_agent_lives_in_its_own_module() -> None:
    from ecs_agents.agents.billing.gst_tax_engine.eway_bill import AGENT as eway
    from ecs_agents.agents.crm.customer_360_service.customer_360 import AGENT as c360
    from ecs_agents.agents.crm.customer_360_service.customer_360 import Customer360Agent
    from ecs_agents.agents.oms.order_orchestrator.checkout_saga import AGENT as saga
    from ecs_agents.agents.oms.order_orchestrator.checkout_saga import CheckoutSagaAgent
    from ecs_agents.catalog import get_agent

    assert isinstance(saga, CheckoutSagaAgent)
    assert saga.key == "oms.order-orchestrator.checkout-saga"
    assert eway.key == "billing.gst-tax-engine.eway-bill"
    assert "place_order" in saga.system_prompt
    assert get_agent(saga.key) is saga
    assert isinstance(c360, Customer360Agent)
    assert "get_profile" in c360.system_prompt
    assert callable(saga.compile)
    assert callable(saga.ainvoke)

