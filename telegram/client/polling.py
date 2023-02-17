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
            try:
                raw_updates = await self._http.get_updates(
                    offset,
                    limit,
                    timeout,
                    allowed_updates
                )
                updates = [Update.from_dict(update_data) for update_data in raw_updates]

            except Exception as e:
                logging.exception("")
                continue

            for update in updates:
                yield update
                offset = update.update_id + 1

