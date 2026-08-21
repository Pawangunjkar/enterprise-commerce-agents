"""EMI quote.

Domain billing / application subscription-emi-service.
Quote subscription/EMI on principal and tenure.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='subscription-emi-service',
    slug='emi-quote',
    title='EMI quote',
    mission='Quote subscription/EMI on principal and tenure.',
    tools=('subscription-emi-service.emi_quote',),
    keywords=('emi', 'no cost emi', 'tenure'),
)
