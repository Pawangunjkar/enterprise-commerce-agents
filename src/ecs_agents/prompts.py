"""System prompts live on each CommerceAgent; this helper stays for callers."""

from ecs_agents.catalog import get_agent


def prompt_for(agent_key: str) -> str:
    return get_agent(agent_key).system_prompt
