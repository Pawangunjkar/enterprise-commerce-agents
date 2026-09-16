"""DPDP anonymize LangGraph agent.

Domain `crm` / application `dpdp-compliance-service`.
Anonymize a customer under DPDP erasure.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='dpdp-compliance-service',
    slug='dpdp-anonymize',
    title='DPDP anonymize',
    mission='Anonymize a customer under DPDP erasure.',
    tools=('dpdp-compliance-service.anonymize_customer',),
    keywords=('anonymize', 'erasure', 'right to forget'),
)


class DpdpAnonymizeAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `dpdp-compliance-service`. Anonymize a customer under DPDP erasure. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = DpdpAnonymizeAgent()
