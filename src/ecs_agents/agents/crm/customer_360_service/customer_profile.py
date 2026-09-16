"""Customer profile LangGraph agent.

Domain `crm` / application `customer-360-service`.
Upsert PAN/GSTIN/name on the 360 profile.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='customer-360-service',
    slug='customer-profile',
    title='Customer profile',
    mission='Upsert PAN/GSTIN/name on the 360 profile.',
    tools=('customer-360-service.upsert_profile',),
    keywords=('customer profile', 'gstin profile', 'pan'),
)


class CustomerProfileAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `customer-360-service`. Upsert PAN/GSTIN/name on the 360 profile. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = CustomerProfileAgent()
