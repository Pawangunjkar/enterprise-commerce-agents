from ecs_agents.scenarios import list_scenario_ids, load_scenario
from ecs_agents.registry import AGENTS


def test_every_scenario_maps_to_a_known_agent() -> None:
    ids = list_scenario_ids()
    assert "checkout-delhi-upi" in ids
    assert "mec-catalog-lifecycle" in ids
    assert "mec-offer-promo" in ids
    assert "crm-assisted-sales-paylink" in ids
    assert "oms-order-to-fulfillment" in ids
    for scenario_id in ids:
        spec = load_scenario(scenario_id)
        assert spec["agent"] in AGENTS
        assert spec["steps"]
        for step in spec["steps"]:
            assert "." in step["call"]
