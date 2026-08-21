"""Master admin audit.

Domain portal / application master-admin-portal.
Ops audit query from master admin.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='portal',
    application='master-admin-portal',
    slug='ops-audit',
    title='Master admin audit',
    mission='Ops audit query from master admin.',
    tools=('master-admin-portal.list_audit',),
    keywords=('master admin audit',),
)
