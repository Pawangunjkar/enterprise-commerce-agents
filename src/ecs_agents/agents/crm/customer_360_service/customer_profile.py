"""Customer profile.

Domain crm / application customer-360-service.
Upsert PAN/GSTIN/name on the 360 profile.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='customer-360-service',
    slug='customer-profile',
    title='Customer profile',
    mission='Upsert PAN/GSTIN/name on the 360 profile.',
    tools=('customer-360-service.upsert_profile',),
    keywords=('customer profile', 'gstin profile', 'pan'),
)
