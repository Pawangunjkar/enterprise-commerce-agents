"""Offer authoring.

Domain mec / application offer-promotion-service.
Create a live promotion/offer.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='offer-promotion-service',
    slug='offer-create',
    title='Offer authoring',
    mission='Create a live promotion/offer.',
    tools=('offer-promotion-service.create_offer',),
    keywords=('create offer', 'promotion', 'festival offer'),
)
