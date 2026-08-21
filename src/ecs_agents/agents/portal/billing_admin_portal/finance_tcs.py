"""Billing admin TCS.

Domain portal / application billing-admin-portal.
Finance TCS from billing admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='billing-admin-portal',
    slug='finance-tcs',
    title='Billing admin TCS',
    mission='Finance TCS from billing admin.',
    tools=('billing-admin-portal.compute_tcs_194o',),
    keywords=('billing admin tcs',),
)
