"""Payment plugin health LangGraph agent.

Domain `billing` / application `payment-gateway-plugins`.
Payment plugin process probe.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='payment-gateway-plugins',
    slug='plugin-health',
    title='Payment plugin health',
    mission='Payment plugin process probe.',
    tools=('payment-gateway-plugins.health',),
    keywords=('payment plugin', 'psp plugin'),
)


class PluginHealthAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `payment-gateway-plugins`. Payment plugin process probe. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = PluginHealthAgent()
