"""CPQ rules LangGraph agent.

Domain `mec` / application `cpq-rule-engine`.
Evaluate configure-price-quote rules on a payload.
"""

from ecs_agents.agents.base import CommerceAgent
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


class CpqEvaluateAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `cpq-rule-engine`. Evaluate configure-price-quote rules on a payload. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CpqEvaluateAgent()
