"""Bundle pricing LangGraph agent.

Domain `mec` / application `component-bundle-service`.
Price a component bundle / kit.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='component-bundle-service',
    slug='bundle-price',
    title='Bundle pricing',
    mission='Price a component bundle / kit.',
    tools=('component-bundle-service.price_bundle',),
    keywords=('bundle', 'kit price'),
)


class BundlePriceAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `component-bundle-service`. Price a component bundle / kit. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = BundlePriceAgent()
