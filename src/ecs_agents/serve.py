from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ecs_agents.graph import chat_once
from ecs_agents.mcp_hub import McpHub
from ecs_agents.registry import agents_by_domain, unique_agents
from ecs_agents.scenarios import list_scenario_ids, run_scenario
from ecs_agents.settings import load_settings

app = FastAPI(
    title="Enterprise Commerce Agents",
    description="LangGraph operators per domain and application. Owner: Pawan Gunjkar.",
    version="1.0.0",
)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/v1/agents")
def agents(domain: str | None = None, application: str | None = None) -> dict:
    specs = unique_agents()
    if domain:
        specs = [s for s in specs if s.domain == domain]
    if application:
        specs = [s for s in specs if s.application == application]
    return {
        "count": len(specs),
        "agents": [
            {
                "key": spec.key,
                "domain": spec.domain,
                "application": spec.application,
                "slug": spec.slug,
                "title": spec.title,
                "mission": spec.mission,
                "kind": spec.kind,
                "mcpServers": list(spec.servers),
                "tools": list(spec.tools),
                "defaultScenario": spec.default_scenario or None,
            }
            for spec in specs
        ],
    }


@app.get("/v1/domains")
def domains() -> dict:
    tree = agents_by_domain()
    return {
        "domains": {
            domain: {app: [spec.key for spec in agents] for app, agents in apps.items()}
            for domain, apps in tree.items()
        }
    }


@app.get("/v1/scenarios")
def scenarios() -> dict:
    return {"scenarios": list_scenario_ids()}


@app.post("/v1/chat")
async def chat(body: ChatRequest) -> dict:
    settings = load_settings()
    async with McpHub(settings) as hub:
        reply = await chat_once(settings, hub, body.message)
    return {"reply": reply}


@app.post("/v1/scenarios/{scenario_id}/run")
async def run(scenario_id: str) -> dict:
    if scenario_id not in list_scenario_ids():
        raise HTTPException(404, f"Unknown scenario {scenario_id}")
    settings = load_settings()
    async with McpHub(settings) as hub:
        return await run_scenario(hub, scenario_id)
