import json

import requests


def send_discord(url: str, message: str) -> bool:
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps({"content": message}),
    )

    return response.status_code == 204
