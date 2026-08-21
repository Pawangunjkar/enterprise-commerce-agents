"""Payment plugin health.

Domain billing / application payment-gateway-plugins.
Payment plugin process probe.
"""

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
