from ecs_agents.catalog import get_agent
from ecs_agents.enrichment import PLAYBOOKS, playbook_prompt
from ecs_agents.registry import AGENTS
from ecs_agents.scenarios import list_scenario_ids, load_scenario


def test_playbooks_cover_crm_oms_mec() -> None:
    assert "crm-full" in PLAYBOOKS
    assert "crm-assisted-sales" in PLAYBOOKS
    assert "oms-checkout" in PLAYBOOKS
    assert "oms-fulfillment" in PLAYBOOKS
    assert "mec-catalog-lifecycle" in PLAYBOOKS
    assert "mec-b2b-quote" in PLAYBOOKS
    assert "mec-offer-promo" in PLAYBOOKS


def test_playbook_prompt_includes_ordered_steps() -> None:
    prompt = playbook_prompt("crm-full")
    assert "otp_start" in prompt
    assert "otp_verify" in prompt
    assert "mark_abandoned" in prompt


def test_enriched_agents_reference_playbooks() -> None:
    c360 = get_agent("crm.customer-360-service.customer-360")
    checkout = get_agent("checkout")
    mec = get_agent("mec-catalog")
    assert "crm-full" in c360.system_prompt
    assert "cart-service.add_cart_item" in checkout.system_prompt
    assert "b2b-tiered-catalog-service.b2b_quote" in mec.system_prompt


def test_new_scenarios_map_to_agents() -> None:
    ids = list_scenario_ids()
    assert "mec-catalog-lifecycle" in ids
    assert "mec-b2b-tier-quote" in ids
    assert "mec-offer-promo" in ids
    assert "crm-assisted-sales-paylink" in ids
    assert "oms-order-to-fulfillment" in ids
    for scenario_id in (
        "mec-catalog-lifecycle",
        "mec-b2b-tier-quote",
        "mec-offer-promo",
        "crm-assisted-sales-paylink",
        "oms-order-to-fulfillment",
    ):
        spec = load_scenario(scenario_id)
        assert spec["agent"] in AGENTS
        assert len(spec["steps"]) >= 4
