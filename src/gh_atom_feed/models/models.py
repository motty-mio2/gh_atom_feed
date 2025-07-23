from pydantic import BaseModel, Field


class Request(BaseModel):
    github_url: str
    discord_webhook: str = Field(default="")
    hour: int = 0


class Update(BaseModel):
    url: str
    title: str
    content: str


class Response(BaseModel):
    status: bool
    updates: int
