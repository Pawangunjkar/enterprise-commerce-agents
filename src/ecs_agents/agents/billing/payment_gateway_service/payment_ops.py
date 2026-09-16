"""Payment ops LangGraph agent.

Domain `billing` / application `payment-gateway-service`.
Poll payment status or simulate capture.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='payment-gateway-service',
    slug='payment-ops',
    title='Payment ops',
    mission='Poll payment status or simulate capture.',
    tools=('payment-gateway-service.payment_status', 'payment-gateway-service.simulate_success'),
    keywords=('payment status', 'simulate success', 'upi status'),
)


class PaymentOpsAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `payment-gateway-service`. Poll payment status or simulate capture. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = PaymentOpsAgent()
