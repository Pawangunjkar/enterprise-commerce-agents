"""MCA audit query.

Domain platform / application mca-audit-trail-service.
Page audit events by resource type.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='mca-audit-trail-service',
    slug='audit-query',
    title='MCA audit query',
    mission='Page audit events by resource type.',
    tools=('mca-audit-trail-service.list_audit',),
    keywords=('list audit', 'audit trail'),
)
