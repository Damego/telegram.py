import logging
from typing import AsyncGenerator

from ..http.client import HTTPClient
from ..models.telegram import Update


class Polling:
    def __init__(self, http: HTTPClient):
        self._http = http

    async def polling(
        self,
        offset: int | None = None,
        limit: int | None = None,
        timeout: int = 30,
        allowed_updates: list[str] | None = None
    ) -> AsyncGenerator[Update, None]:
        while True:
            raw_updates = await self._http.get_updates(
                offset,
                limit,
                timeout,
                allowed_updates
            )
            updates = Update.from_list(raw_updates, self._http)

            for update in updates:
                yield update
                offset = update.update_id + 1

