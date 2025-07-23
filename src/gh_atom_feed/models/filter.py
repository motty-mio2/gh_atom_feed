import datetime

from pydantic import BaseModel


class Filter(BaseModel):
    day: int = 0
    hour: int = 0
    minute: int = 0

    def ISO8601(self) -> str:
        dt = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
            days=self.day,
            hours=self.hour,
            minutes=self.minute,
        )
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
