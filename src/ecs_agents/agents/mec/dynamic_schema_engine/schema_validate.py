"""Dynamic schema.

Domain mec / application dynamic-schema-engine.
Validate attribute payloads against catalog schema.
"""

from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='dynamic-schema-engine',
    slug='schema-validate',
    title='Dynamic schema',
    mission='Validate attribute payloads against catalog schema.',
    tools=('dynamic-schema-engine.validate_schema',),
    keywords=('schema', 'attribute validate'),
)
