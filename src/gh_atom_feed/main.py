from fastapi import FastAPI

from .functions import parse_atom_feed
from .models import Request, Response

app = FastAPI()


@app.post("/")
def read_root(item: Request) -> Response:
    result = parse_atom_feed(item.url, item.hour)
    return Response(status=True, updates=result)
