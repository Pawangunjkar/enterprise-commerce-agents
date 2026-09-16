"""Load OpenAI or Gemini chat models for LangGraph ReAct."""

from __future__ import annotations

from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel

from ecs_agents.settings import Settings


def load_llm(settings: Settings) -> BaseChatModel | None:
    provider = settings.resolved_llm_provider
    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model=settings.gemini_model,
            google_api_key=settings.gemini_api_key,
            temperature=0,
        )
    if provider == "openai":
        from langchain_openai import ChatOpenAI

        kwargs: dict[str, Any] = {
            "model": settings.openai_model,
            "api_key": settings.openai_api_key,
            "temperature": 0,
        }
        if settings.openai_base_url:
            kwargs["base_url"] = settings.openai_base_url
        return ChatOpenAI(**kwargs)
    return None


def llm_setup_hint(settings: Settings) -> str:
    return (
        "Set LLM_PROVIDER=openai|gemini and OPENAI_API_KEY or "
        "GEMINI_API_KEY (or GOOGLE_API_KEY) so this LangGraph ReAct agent can call MCP tools"
        + (f" (resolved provider would be `{settings.llm_provider}`)." if settings.llm_provider else ".")
    )
