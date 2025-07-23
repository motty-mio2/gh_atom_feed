from typing import Any

from pydantic import BaseModel


class Commit(BaseModel):
    url: str
    message: str

    def to_discord(self) -> tuple[str, list[dict[str, Any]]]:
        return (
            "new_commit",
            [
                {
                    "title": self.message,
                    "url": self.url,
                }
            ],
        )
