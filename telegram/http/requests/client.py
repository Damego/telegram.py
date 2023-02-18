from typing import cast

from ...utils.serializer import dict_filter_none_and_self
from ..route import Route
from ...models.protocols import BaseRequest


class ClientRequests(BaseRequest):
    async def get_updates(
        self,
        offset: int | None = None,
        limit: int | None = None,
        timeout: int | None = None,
        allowed_updates: list[str] | None = None
    ) -> list[dict]:
        data = dict_filter_none_and_self(**locals())
        response = await self.request(Route("GET", "/getUpdates"), data)

        return cast(list[dict], response)

    async def get_me(self) -> dict:
        response = await self.request(Route("GET", "/getMe"))
        return cast(dict, response)




