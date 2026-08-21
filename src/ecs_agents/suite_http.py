from __future__ import annotations

import json
from typing import Any

import httpx

from ecs_agents.settings import Settings


class SuiteHttp:
    """Direct suite calls for APIs not yet regenerated into MCP servers (recommendations, get order)."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.headers = {
            "Accept": "application/json",
            "X-Tenant-Id": settings.tenant_id,
        }
        if settings.bearer_token:
            self.headers["Authorization"] = f"Bearer {settings.bearer_token}"

    def request(self, method: str, path: str, json_body: Any | None = None) -> Any:
        url = f"{self.settings.gateway_url}{path}"
        with httpx.Client(timeout=self.settings.http_timeout, headers=self.headers) as client:
            response = client.request(method, url, json=json_body)
        if response.status_code >= 400:
            return {"error": f"{response.status_code} {url}", "body": response.text[:1500]}
        if not response.content:
            return {"ok": True, "status": response.status_code}
        if "json" in response.headers.get("content-type", ""):
            return response.json()
        return {"ok": True, "body": response.text[:2000]}

    def recommend(self, skus: list[str], limit: int = 5) -> Any:
        return self.request("POST", "/api/v1/recommendations", {"skus": skus, "limit": limit})

    def get_order(self, order_id: str) -> Any:
        return self.request("GET", f"/api/v1/orders/{order_id}")


def extra_tool_specs() -> list[dict[str, Any]]:
    return [
        {
            "name": "suite.recommend_skus",
            "description": "OMS cross-sell and up-sell from live affinity rules and SKU ladder. Pass cart SKUs.",
            "kind": "recommend",
        },
        {
            "name": "suite.get_order",
            "description": "Load a persisted commerce order by UUID after place_order.",
            "kind": "get_order",
        },
    ]


def invoke_extra(http: SuiteHttp, name: str, arguments: dict[str, Any]) -> Any:
    if name.endswith("recommend_skus") or name == "suite.recommend_skus":
        skus = arguments.get("skus") or []
        if isinstance(skus, str):
            skus = [s.strip() for s in skus.split(",") if s.strip()]
        return http.recommend(list(skus), int(arguments.get("limit") or 5))
    if name.endswith("get_order") or name == "suite.get_order":
        return http.get_order(str(arguments.get("orderId") or arguments.get("order_id") or ""))
    return {"error": f"unknown extra tool {name}"}


def dump(value: Any) -> str:
    return json.dumps(value, default=str)
