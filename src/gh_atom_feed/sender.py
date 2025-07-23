import json
from typing import Any

import requests


def send_discord(
    url: str, content: str | None = None, embeds: dict[str, Any] | None = None
) -> bool:
    if content is None and embeds is None:
        return False

    data: dict[str, Any] = {}

    if content:
        data["content"] = content

    if embeds:
        data["embeds"] = embeds

    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(data),
    )

    return response.status_code == 204
