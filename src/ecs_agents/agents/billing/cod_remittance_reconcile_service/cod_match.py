"""COD remittance.

Domain billing / application cod-remittance-reconcile-service.
Match COD remittance vs carrier and bank amounts.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='cod-remittance-reconcile-service',
    slug='cod-match',
    title='COD remittance',
    mission='Match COD remittance vs carrier and bank amounts.',
    tools=('cod-remittance-reconcile-service.match_cod',),
    keywords=('cod remittance', 'cod match'),
)
