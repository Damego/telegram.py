from attrs import field

from ..attrs_utils import ClientSerializerMixin, convert_dataclass, define
from .user import User
from .message import Message


@define()
class CallbackQuery(ClientSerializerMixin):
    id: str
    user: User = field(default=None, converter=convert_dataclass(User))
    message: Message | None = field(default=None, converter=convert_dataclass(Message))
    inline_message_id: str | None = field(default=None)
    chat_instance: str | None = field(default=None)
    data: str | None = field(default=None)
    game_short_name: str | None = field(default=None)

    @classmethod
    def process_dict(cls, data: dict, http) -> dict:
        if "from" in data:
            data["user"] = data.pop("from")

        return super().process_dict(data, http)


@define()
class Update(ClientSerializerMixin):
    update_id: int
    message: Message | None = field(converter=convert_dataclass(Message), default=None)
    edited_message: Message | None = field(converter=convert_dataclass(Message), default=None)
    channel_post: Message | None = field(converter=convert_dataclass(Message), default=None)
    edited_channel_post: Message | None = field(converter=convert_dataclass(Message), default=None)
    # inline_query
    # chosen_inline_result
    callback_query: CallbackQuery | None = field(converter=convert_dataclass(CallbackQuery), default=None)
    # shipping_query
    # pre_checkout_query
    # poll
    # poll_answer
    # my_chat_member
    # chat_member
    # chat_join_request

