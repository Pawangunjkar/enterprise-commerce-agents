from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ecs_agents.graph import chat_once
from ecs_agents.mcp_hub import McpHub
from ecs_agents.registry import AGENTS
from ecs_agents.scenarios import list_scenario_ids, run_scenario
from ecs_agents.settings import load_settings

app = FastAPI(
    title="Enterprise Commerce Agents",
    description="LangGraph operators that call live suite data through MCP. Owner: Pawan Gunjkar.",
    version="1.0.0",
)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)


class ScenarioRun(BaseModel):
    scenario: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/v1/agents")
def agents() -> dict:
    return {
        "agents": [
            {
                "key": spec.key,
                "title": spec.title,
                "mission": spec.mission,
                "mcpServers": list(spec.servers),
                "defaultScenario": spec.default_scenario,
            }
            for spec in AGENTS.values()
        ]
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
