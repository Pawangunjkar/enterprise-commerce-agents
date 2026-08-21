"""CPQ rules.

Domain mec / application cpq-rule-engine.
Evaluate configure-price-quote rules on a payload.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='cpq-rule-engine',
    slug='cpq-evaluate',
    title='CPQ rules',
    mission='Evaluate configure-price-quote rules on a payload.',
    tools=('cpq-rule-engine.evaluate_cpq',),
    keywords=('cpq', 'configure price'),
)
