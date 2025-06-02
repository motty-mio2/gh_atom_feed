from pydantic import BaseModel


class Request(BaseModel):
    url: str
    hour: int = 0


class Update(BaseModel):
    url: str
    title: str
    content: str


class Response(BaseModel):
    status: bool
    updates: list[Update] = []
