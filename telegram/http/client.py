from aiohttp import ClientSession

import orjson

from .route import Route
from .request import Request


class HTTPClient(
    Request
):
    def __init__(self, token: str):
        self._session: ClientSession | None = None
        Route.token = token

    async def get_client_session(self) -> ClientSession:
        if self._session is None or self._session.closed:
            self._session = ClientSession()

        return self._session

    async def request(self, route: Route, data: dict):
        await self.get_client_session()

        async with self._session.request(route.method, route.url, params=data) as response:
            json = await response.json(loads=orjson.loads)

            # TODO: ratelimits
            if json["ok"]:
                return json["result"]
            print(json)

