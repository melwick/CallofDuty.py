import logging

from .enums import Platform
from .match import Match

log = logging.getLogger(__name__)


class User:
    def __init__(self, http: object, platform: str, username: str):
        self.http = http
        self.platform = Platform(platform)
        self.username = username

    async def profile(self):
        return await self.http.GetProfile(self.platform.value, self.username)

    async def matches(self, count: int = 0, lazy: bool = True):
        data = await self.http.GetRecentMatches(self.platform.value, self.username)

        matches = []

        if data["data"]["matches"] == None:
            return None

        for it in data["data"]["matches"]:
            match = Match(self.http, self.platform, it)
            matches.append(match)

            # For clarity
            if lazy == False:
                match.teams()

        return matches
