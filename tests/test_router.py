from ecs_agents.registry import route_agent
from ecs_agents.scenarios import resolve_value


def test_routes_gst_to_tax_desk() -> None:
    assert route_agent("Compute IGST and e-way bill for MH") == "tax"


def test_routes_recommendations_to_merchandising() -> None:
    assert route_agent("Show cross-sell and upsell for this SKU") == "merchandising"


def test_routes_ndr_to_fulfillment() -> None:
    assert route_agent("Reattempt NDR for this AWB") == "fulfillment"


def test_jsonpath_walks_nested_and_data_wrapper() -> None:
    ctx = {"order": {"data": {"orderId": "abc-123"}, "success": True}}
    assert resolve_value("$.order.data.orderId", ctx) == "abc-123"
    assert resolve_value("$.order.orderId", ctx) == "abc-123"


def test_jsonpath_in_args() -> None:
    ctx = {"order": {"data": {"orderId": "oid-9"}}}
    args = resolve_value({"orderId": "$.order.data.orderId", "amount": 10}, ctx)
    assert args == {"orderId": "oid-9", "amount": 10}
