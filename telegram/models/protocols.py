from typing import Protocol

from ..http.route import Route


class BaseRequest(Protocol):
    async def request(self, route: Route, data: dict | None = None) -> dict:
        raise NotImplementedError()