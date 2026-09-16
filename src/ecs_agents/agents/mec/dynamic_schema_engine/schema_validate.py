"""Dynamic schema LangGraph agent.

Domain `mec` / application `dynamic-schema-engine`.
Validate attribute payloads against catalog schema.
"""

from ecs_agents.agents.base import CommerceAgent
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


class SchemaValidateAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `dynamic-schema-engine`. Validate attribute payloads against catalog schema. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = SchemaValidateAgent()
