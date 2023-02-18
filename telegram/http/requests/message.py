from typing import cast

from ...utils.serializer import dict_filter_none_and_self
from ..route import Route
from ...models.protocols import BaseRequest


class MessageRequests(BaseRequest):
    async def send_message(
        self,
        chat_id: int,
        text: str,
        message_thread_id: int | None = None,
        parse_mode: str | None = None,
        entities: list[dict] | None = None,
        disable_web_page_preview: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: dict | None = None,
    ) -> dict:
        data = dict_filter_none_and_self(**locals())
        response = await self.request(Route("POST", "/sendMessage"), data)
        return cast(dict, response)
