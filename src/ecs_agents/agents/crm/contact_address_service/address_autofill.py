"""Address autofill.

Domain crm / application contact-address-service.
Autofill address from pincode master.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='contact-address-service',
    slug='address-autofill',
    title='Address autofill',
    mission='Autofill address from pincode master.',
    tools=('contact-address-service.autofill_address',),
    keywords=('autofill', 'address pincode'),
)
