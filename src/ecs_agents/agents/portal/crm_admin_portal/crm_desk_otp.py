"""CRM admin OTP.

Domain portal / application crm-admin-portal.
Assisted OTP from CRM admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='crm-admin-portal',
    slug='crm-desk-otp',
    title='CRM admin OTP',
    mission='Assisted OTP from CRM admin.',
    tools=('crm-admin-portal.otp_start',),
    keywords=('crm admin otp',),
)
