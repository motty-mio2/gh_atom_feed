from email import message

from fastapi import FastAPI

from gh_atom_feed.functions.github import Github
from gh_atom_feed.models.filter import Filter
from gh_atom_feed.models.models import Request, Response
from gh_atom_feed.sender import send_discord

app = FastAPI()


@app.post("/")
def read_root(item: Request) -> Response:
    gh = Github()

    filter = Filter(hour=item.hour)

    commits = gh.get_commits(item.github_url, filter)
    issues = gh.get_issues(item.github_url, filter)
    comments = gh.get_issue_comments(item.github_url, filter)

    status = True

    for c in [*commits, *issues, *comments]:
        content, embeds = c.to_discord()  # type: ignore
        send_discord(
            item.discord_webhook,
            content=content,
            embeds=embeds,
        )

    return Response(status=status, updates=len(commits) + len(issues) + len(comments))
