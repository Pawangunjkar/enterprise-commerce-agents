"""Billing admin ledger.

Domain portal / application billing-admin-portal.
Finance journal from billing admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='billing-admin-portal',
    slug='finance-ledger',
    title='Billing admin ledger',
    mission='Finance journal from billing admin.',
    tools=('billing-admin-portal.post_journal',),
    keywords=('billing admin ledger',),
)
