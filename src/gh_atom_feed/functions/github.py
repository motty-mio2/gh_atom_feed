import requests

from gh_atom_feed.models.commit import Commit
from gh_atom_feed.models.filter import Filter
from gh_atom_feed.models.issue import Comment, Issue


class Github:
    def __init__(self, token: str = "") -> None:
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        if self.token:
            self.headers["Authorization"] = f"Bearer {self.token}"

    def get_commits(self, repo_path: str, filter: Filter) -> list[Commit]:
        url = f"{self.base_url}/repos/{repo_path}/commits"
        response = requests.get(
            url,
            headers=self.headers,
            params={
                "since": filter.ISO8601(),
            },
        )
        response.raise_for_status()
        data = response.json()

        ret = []

        for d in data:
            commit = Commit(url=d["html_url"], message=d["commit"]["message"])

            ret.append(commit)

        return ret

    def get_issues(self, repo_path: str, filter: Filter) -> list[Issue]:
        """
        Fetches a specific issue by its number.
        """
        url = f"{self.base_url}/repos/{repo_path}/issues"
        response = requests.get(
            url,
            headers=self.headers,
            params={
                "since": filter.ISO8601(),
            },
        )
        response.raise_for_status()
        data = response.json()

        ret = []

        for d in data:
            issue = Issue(
                url=d["html_url"],
                title=d["title"],
                author=d["user"]["login"],
                avatar_url=d["user"]["avatar_url"],
            )

            ret.append(issue)

        return ret

    def get_issue_comments(self, repo_path: str, filter: Filter) -> list[Comment]:
        """
        Fetches comments for a specific issue.
        """
        url = f"{self.base_url}/repos/{repo_path}/issues/comments"
        response = requests.get(
            url,
            headers=self.headers,
            params={
                "since": filter.ISO8601(),
            },
        )
        response.raise_for_status()
        data = response.json()

        ret = []

        for d in data:
            comment = Comment(
                url=d["html_url"],
                body=d["body"],
                author=d["user"]["login"],
                avatar_url=d["user"]["avatar_url"],
            )

            ret.append(comment)

        return ret
