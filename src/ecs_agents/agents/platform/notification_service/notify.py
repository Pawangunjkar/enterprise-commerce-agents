"""Notification dispatch LangGraph agent.

Domain `platform` / application `notification-service`.
Send SMS/email/WhatsApp templates (OTP, order).
"""

from ecs_agents.agents.base import CommerceAgent
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


class NotifyAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `notification-service`. Send SMS/email/WhatsApp templates (OTP, order). Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = NotifyAgent()
