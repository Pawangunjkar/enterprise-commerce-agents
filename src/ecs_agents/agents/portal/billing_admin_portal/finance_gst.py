"""Billing admin GST.

Domain portal / application billing-admin-portal.
Finance GST compute from billing admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='billing-admin-portal',
    slug='finance-gst',
    title='Billing admin GST',
    mission='Finance GST compute from billing admin.',
    tools=('billing-admin-portal.compute_gst',),
    keywords=('billing admin gst',),
)
