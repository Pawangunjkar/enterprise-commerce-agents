"""BharatQR.

Domain billing / application payment-gateway-service.
Mint dynamic UPI BharatQR and intent URLs.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='payment-gateway-service',
    slug='bharat-qr',
    title='BharatQR',
    mission='Mint dynamic UPI BharatQR and intent URLs.',
    tools=('payment-gateway-service.create_bharat_qr',),
    keywords=('bharatqr', 'bharat qr', 'upi qr'),
)
