import datetime

import feedparser

from gh_atom_feed.models import Update


def parse_atom_feed(url: str, hour: int) -> list[Update]:
    d_atom = feedparser.parse(url)

    ret: list[Update] = []

    for entry in d_atom.entries:
        updated_time = datetime.datetime.strptime(
            str(entry["updated"]), "%Y-%m-%dT%H:%M:%SZ"
        ).replace(tzinfo=datetime.timezone.utc)
        now = datetime.datetime.now(datetime.timezone.utc)
        time_diff = now - updated_time

        if time_diff < datetime.timedelta(hours=hour):
            ret.append(
                Update(
                    url=str(entry["link"]),
                    title=str(entry["title"]),
                    content=str(
                        entry.get("summary", ""),
                    ),
                )
            )
        else:
            break

    return ret
