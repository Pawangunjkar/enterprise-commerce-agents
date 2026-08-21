"""Payment ops.

Domain billing / application payment-gateway-service.
Poll payment status or simulate capture.
"""

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
