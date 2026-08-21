"""B2B account tree.

Domain crm / application account-hierarchy-service.
Read dealer/distributor account hierarchy.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='account-hierarchy-service',
    slug='account-tree',
    title='B2B account tree',
    mission='Read dealer/distributor account hierarchy.',
    tools=('account-hierarchy-service.account_tree',),
    keywords=('account tree', 'b2b hierarchy'),
)
