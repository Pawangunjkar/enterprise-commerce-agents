"""OMS merchandising LangGraph agent.

Domain `oms` / application `order-orchestrator`.
Cross-sell and up-sell from affinity rules and SKU ladder.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='oms',
    application='order-orchestrator',
    slug='merchandising',
    title='OMS merchandising',
    mission='Cross-sell and up-sell from affinity rules and SKU ladder.',
    tools=('suite.recommend_skus',),
    keywords=('cross-sell', 'upsell', 'up-sell', 'recommend', 'affinity'),
    scenario='merchandising-upsell',
)


class MerchandisingAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `order-orchestrator`. Cross-sell and up-sell from affinity rules and SKU ladder. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = MerchandisingAgent()
