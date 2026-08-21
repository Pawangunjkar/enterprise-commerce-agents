"""General ledger.

Domain billing / application general-ledger-service.
Post a GAAP journal entry.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='billing',
    application='general-ledger-service',
    slug='ledger-post',
    title='General ledger',
    mission='Post a GAAP journal entry.',
    tools=('general-ledger-service.post_journal',),
    keywords=('journal', 'general ledger', 'gaap'),
)
