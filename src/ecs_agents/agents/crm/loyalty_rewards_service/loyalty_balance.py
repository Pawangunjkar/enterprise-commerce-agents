"""Loyalty balance.

Domain crm / application loyalty-rewards-service.
Read loyalty points with festival multiplier.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='loyalty-rewards-service',
    slug='loyalty-balance',
    title='Loyalty balance',
    mission='Read loyalty points with festival multiplier.',
    tools=('loyalty-rewards-service.get_loyalty',),
    keywords=('loyalty', 'reward points', 'festival multiplier'),
)
