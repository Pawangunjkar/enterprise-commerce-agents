"""Notification dispatch.

Domain platform / application notification-service.
Send SMS/email/WhatsApp templates (OTP, order).
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='notification-service',
    slug='notify',
    title='Notification dispatch',
    mission='Send SMS/email/WhatsApp templates (OTP, order).',
    tools=('notification-service.send_notification',),
    keywords=('sms', 'whatsapp', 'notification'),
)
