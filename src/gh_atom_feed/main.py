from fastapi import FastAPI

from .functions import parse_atom_feed
from .models import Request, Response
from .sender import send_discord

app = FastAPI()


@app.post("/")
def read_root(item: Request) -> Response:
    result = parse_atom_feed(item.github_url, item.hour)

    if item.discord_webhook:
        for update in result:
            send_discord(item.discord_webhook, f"{update.title}\n{update.content}")

    return Response(status=True, updates=len(result))
