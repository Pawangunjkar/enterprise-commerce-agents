from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    gateway_url: str
    tenant_id: str
    bearer_token: str
    http_timeout: float
    mcp_python: str
    openai_api_key: str
    openai_model: str
    openai_base_url: str

    @property
    def service_url(self) -> str:
        return self.gateway_url


def load_settings() -> Settings:
    gateway = os.environ.get("ECS_GATEWAY_URL") or os.environ.get("ECS_SERVICE_URL") or "http://localhost:8080"
    return Settings(
        gateway_url=gateway.rstrip("/"),
        tenant_id=os.environ.get("ECS_TENANT_ID", "default"),
        bearer_token=os.environ.get("ECS_BEARER_TOKEN", ""),
        http_timeout=float(os.environ.get("ECS_HTTP_TIMEOUT", "20")),
        mcp_python=os.environ.get("ECS_MCP_PYTHON", "").strip(),
        openai_api_key=os.environ.get("OPENAI_API_KEY", "").strip(),
        openai_model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        openai_base_url=os.environ.get("OPENAI_BASE_URL", "").strip(),
    )
