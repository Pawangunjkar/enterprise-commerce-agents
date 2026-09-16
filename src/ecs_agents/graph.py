from __future__ import annotations

from langchain_core.language_models.chat_models import BaseChatModel
from pydantic import BaseModel, Field

from ecs_agents.catalog import BUNDLE, get_agent, unique_agents
from ecs_agents.llm import load_llm, llm_setup_hint
from ecs_agents.mcp_hub import McpHub
from ecs_agents.registry import route_agent
from ecs_agents.settings import Settings


class RouteDecision(BaseModel):
    agent_key: str = Field(description="Exact agent key from the catalog")
    reason: str = Field(description="Why this operator owns the request")


def _catalog_brief() -> str:
    lines = []
    for spec in unique_agents():
        if spec.kind == "journey":
            continue
        lines.append(f"- {spec.key} | {spec.title} | {spec.mission}")
    return "\n".join(lines)


async def choose_agent(text: str, llm: BaseChatModel | None) -> str:
    keyword_key = route_agent(text)
    if llm is None:
        return keyword_key
    try:
        structured = llm.with_structured_output(RouteDecision)
        decision = await structured.ainvoke(
            [
                (
                    "system",
                    "Pick the single best Enterprise Commerce operator for this job. "
                    "Return an exact agent_key from the list. Prefer specialists over journeys. "
                    "Catalog:\n" + _catalog_brief(),
                ),
                ("human", text),
            ]
        )
        key = decision.agent_key if isinstance(decision, RouteDecision) else keyword_key
        if key in BUNDLE:
            return key
    except Exception:
        return keyword_key
    return keyword_key


async def chat_once(settings: Settings, hub: McpHub, text: str) -> str:
    llm = load_llm(settings)
    key = await choose_agent(text, llm)
    agent = get_agent(key)
    if llm is None:
        hint = agent.spec.default_scenario or agent.key
        return (
            f"No LLM API key. Keyword-routed to {type(agent).__name__} (`{agent.key}`).\n"
            f"{agent.spec.mission}\n"
            f"Tools: {', '.join(agent.spec.tools)}\n"
            f"{llm_setup_hint(settings)}, "
            f"or run: ecs-agents run {hint}"
        )
    return await agent.ainvoke(llm, hub, text)
