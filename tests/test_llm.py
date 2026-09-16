import os
from unittest.mock import MagicMock, patch

from ecs_agents.llm import load_llm
from ecs_agents.settings import load_settings


def _clear_llm_env(monkeypatch) -> None:
    for key in (
        "LLM_PROVIDER",
        "OPENAI_API_KEY",
        "OPENAI_MODEL",
        "OPENAI_BASE_URL",
        "GEMINI_API_KEY",
        "GOOGLE_API_KEY",
        "GOOGLE_GENAI_API_KEY",
        "GEMINI_MODEL",
    ):
        monkeypatch.delenv(key, raising=False)


def test_auto_prefers_openai_when_both_keys(monkeypatch) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    monkeypatch.setenv("GEMINI_API_KEY", "gem-test")
    settings = load_settings()
    assert settings.resolved_llm_provider == "openai"


def test_auto_uses_gemini_without_openai(monkeypatch) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("GEMINI_API_KEY", "gem-test")
    settings = load_settings()
    assert settings.resolved_llm_provider == "gemini"


def test_explicit_gemini_provider(monkeypatch) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("LLM_PROVIDER", "gemini")
    monkeypatch.setenv("GOOGLE_API_KEY", "google-test")
    settings = load_settings()
    assert settings.gemini_api_key == "google-test"
    assert settings.resolved_llm_provider == "gemini"


def test_load_llm_gemini_constructs_chat_model(monkeypatch) -> None:
    _clear_llm_env(monkeypatch)
    monkeypatch.setenv("LLM_PROVIDER", "gemini")
    monkeypatch.setenv("GEMINI_API_KEY", "gem-test")
    monkeypatch.setenv("GEMINI_MODEL", "gemini-2.0-flash")
    settings = load_settings()
    fake = MagicMock(name="ChatGoogleGenerativeAI")
    with patch("langchain_google_genai.ChatGoogleGenerativeAI", return_value=fake) as ctor:
        model = load_llm(settings)
    assert model is fake
    ctor.assert_called_once()
    kwargs = ctor.call_args.kwargs
    assert kwargs["model"] == "gemini-2.0-flash"
    assert kwargs["google_api_key"] == "gem-test"


def test_no_keys_means_no_llm(monkeypatch) -> None:
    _clear_llm_env(monkeypatch)
    for key in list(os.environ):
        if key in {"OPENAI_API_KEY", "GEMINI_API_KEY", "GOOGLE_API_KEY"}:
            monkeypatch.delenv(key, raising=False)
    settings = load_settings()
    assert settings.resolved_llm_provider is None
    assert load_llm(settings) is None
