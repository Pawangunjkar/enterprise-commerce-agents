# Enterprise Commerce Agents

Public open-source project owned by **Pawan Gunjkar** (`pawangunjkar@gmail.com` · [GitHub](https://github.com/Pawangunjkar)). MIT licensed. See `OWNER.md` and `LICENSE`.

Standalone **Python + LangGraph** project. It is **not** inside `enterprise-commerce-suite` and it is **not** a FAQ chatbot.

Agents are **operators**. They call the sibling [enterprise-commerce-mcps](https://github.com/Pawangunjkar/enterprise-commerce-mcps) FastMCP servers, which in turn hit live Enterprise Commerce Suite APIs (GST, ATP, checkout saga, BharatQR, OMS recommendations, CRM, DPDP). If a service is down, the agent returns the MCP/HTTP error — it does not invent an answer.

```mermaid
flowchart LR
  User["Operator / API"] --> LG["LangGraph supervisor"]
  LG --> A1["Checkout"]
  LG --> A2["GST / TCS"]
  LG --> A3["Merchandising"]
  LG --> A4["Fulfillment"]
  LG --> A5["Billing"]
  LG --> A6["CRM 360"]
  A1 --> MCP["enterprise-commerce-mcps stdio"]
  A2 --> MCP
  A3 --> MCP
  A4 --> MCP
  A5 --> MCP
  A6 --> MCP
  MCP --> GW["Suite gateway :8080"]
```

## What you get

| Agent | Business job | MCP servers |
| --- | --- | --- |
| `checkout` | Serviceability → GST → place order saga → BharatQR | pincode, product, cart, ATP, GST, order-orchestrator, payments |
| `tax` | Intra vs inter GST, e-way bill, TCS 194O | gst-tax-engine, tcs-tds-compliance-engine |
| `merchandising` | Cross-sell / up-sell from OMS affinity + catalog | product, order-orchestrator, offers |
| `fulfillment` | ATP lock, WMS wave, NDR action | ATP, WMS, NDR |
| `billing` | Invoice issue, QR, dunning schedule | payments, invoice, dunning, GST |
| `crm` | OTP, DPDP consent, tickets, loyalty | customer-360, tickets, loyalty, abandonment, DPDP |

Named **scenarios** run the same MCP tools in a fixed playbook (no LLM required). Chat uses LangGraph ReAct when `OPENAI_API_KEY` is set.

## Install

```bash
cd enterprise-commerce-mcps
python -m venv .venv
.venv\Scripts\activate
pip install -e .

cd ..\enterprise-commerce-agents
pip install -e ".[dev]"
copy .env.example .env
```

Start the suite (infra + at least gateway, pincode, product, GST, ATP, orders, payments, invoices). Point agents at the gateway:

```
ECS_GATEWAY_URL=http://localhost:8080
ECS_SERVICE_URL=http://localhost:8080
```

## Run live scenarios (no LLM)

```bash
ecs-agents list-agents
ecs-agents list-scenarios
ecs-agents run checkout-delhi-upi
ecs-agents run gst-interstate-eway
ecs-agents run merchandising-upsell
ecs-agents run fulfillment-atp-wave
ecs-agents run billing-invoice-dunning
ecs-agents run crm-otp-ticket-loyalty
```

Each step prints the JSON returned by MCP (orders, tax type, remaining stock, QR payload, etc.).

## LangGraph chat

```bash
set OPENAI_API_KEY=...
ecs-agents chat "Place a UPI order to 110001 for the 8GB phone and show GST"
```

Without an API key, chat only routes to an agent and tells you which scenario to run.

## HTTP API

```bash
ecs-agents serve --port 8099
```

- `GET /v1/agents`
- `GET /v1/scenarios`
- `POST /v1/chat` `{"message":"..."}`
- `POST /v1/scenarios/{id}/run`

## Layout

- `src/ecs_agents/registry.py` — agent → MCP server map
- `src/ecs_agents/mcp_hub.py` — stdio MCP client (`python -m ecs_mcps.<server>`)
- `src/ecs_agents/graph.py` — LangGraph router + ReAct specialists
- `src/ecs_agents/scenarios.py` — playbook runner with `$.step.field` bindings
- `scenarios/*.yaml` — Indian commerce jobs

OMS recommendations (`POST /api/v1/recommendations`) are exposed as `suite.recommend_skus` until that route is regenerated into the order-orchestrator MCP.

## Owner

- Name: Pawan Gunjkar
- Email: pawangunjkar@gmail.com
- GitHub: https://github.com/Pawangunjkar
- Visibility: public open source (MIT)
