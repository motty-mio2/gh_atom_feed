from typing import Any

from pydantic import BaseModel


class Issue(BaseModel):
    url: str
    title: str
    author: str
    avatar_url: str

    def to_discord(self) -> tuple[str, list[dict[str, Any]]]:
        return (
            "new_issue" if "/issues/" in self.url else "new_pull_request",
            [
                {
                    "title": self.title,
                    "url": self.url,
                    "author": {
                        "name": self.author,
                        "url": f"https://github.com/{self.author}",
                        "icon_url": self.avatar_url,
                    },
                }
            ],
        )


class Comment(BaseModel):
    url: str
    body: str
    author: str
    avatar_url: str

    def to_discord(self) -> tuple[str, list[dict[str, Any]]]:
        return (
            "new_comment",
            [
                {
                    "description": self.body,
                    "url": self.url,
                    "title": f"Comment by {self.author}",
                    "author": {
                        "name": self.author,
                        "url": f"https://github.com/{self.author}",
                        "icon_url": self.avatar_url,
                    },
                }
            ],
        )
