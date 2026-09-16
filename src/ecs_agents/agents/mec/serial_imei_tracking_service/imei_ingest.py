"""IMEI ingest LangGraph agent.

Domain `mec` / application `serial-imei-tracking-service`.
Ingest 15-digit IMEI with Luhn checks.
"""

from ecs_agents.agents.base import CommerceAgent
from ecs_agents.agents.spec import specialist

SPEC = specialist(
    domain='mec',
    application='serial-imei-tracking-service',
    slug='imei-ingest',
    title='IMEI ingest',
    mission='Ingest 15-digit IMEI with Luhn checks.',
    tools=('serial-imei-tracking-service.ingest_imei',),
    keywords=('imei', 'serial ingest', 'luhn'),
)


class ImeiIngestAgent(CommerceAgent):
    spec = SPEC
    instructions = 'You are the dedicated operator for application `serial-imei-tracking-service`. Ingest 15-digit IMEI with Luhn checks. Use only your bound tools. Extract ids, amounts, pincodes, HSN, and SKUs from the user message.'


AGENT = ImeiIngestAgent()
