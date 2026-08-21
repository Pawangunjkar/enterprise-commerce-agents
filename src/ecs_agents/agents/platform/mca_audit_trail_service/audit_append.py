"""MCA audit append.

Domain platform / application mca-audit-trail-service.
Write an MCA-style audit event.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='platform',
    application='mca-audit-trail-service',
    slug='audit-append',
    title='MCA audit append',
    mission='Write an MCA-style audit event.',
    tools=('mca-audit-trail-service.append_audit',),
    keywords=('append audit', 'audit write'),
)
