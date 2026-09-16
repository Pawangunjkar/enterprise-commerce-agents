"""Support ticket LangGraph agent.

Domain `crm` / application `support-ticket-service`.
Open a live support ticket.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='crm',
    application='support-ticket-service',
    slug='ticket-create',
    title='Support ticket',
    mission='Open a live support ticket.',
    tools=('support-ticket-service.create_ticket',),
    keywords=('create ticket', 'support ticket'),
)


class TicketCreateAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `support-ticket-service`. Open a live support ticket. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = TicketCreateAgent()
