"""Cart abandonment.

Domain crm / application cart-abandonment-service.
Mark a cart abandoned for recovery journeys.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='cart-abandonment-service',
    slug='cart-recovery',
    title='Cart abandonment',
    mission='Mark a cart abandoned for recovery journeys.',
    tools=('cart-abandonment-service.mark_abandoned',),
    keywords=('abandon', 'cart recovery'),
)
