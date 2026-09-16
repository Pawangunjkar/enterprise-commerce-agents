"""Address autofill LangGraph agent.

Domain `crm` / application `contact-address-service`.
Autofill address from pincode master.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='contact-address-service',
    slug='address-autofill',
    title='Address autofill',
    mission='Autofill address from pincode master.',
    tools=('contact-address-service.autofill_address',),
    keywords=('autofill', 'address pincode'),
)


class AddressAutofillAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `contact-address-service`. Autofill address from pincode master. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = AddressAutofillAgent()
