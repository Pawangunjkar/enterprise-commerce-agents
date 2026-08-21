"""Pincode master lookup.

Domain platform / application pincode-master-service.
Load India pincode master attributes.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='pincode-master-service',
    slug='pincode-lookup',
    title='Pincode master lookup',
    mission='Load India pincode master attributes.',
    tools=('pincode-master-service.get_pincode',),
    keywords=('pincode lookup', 'pincode master'),
)
