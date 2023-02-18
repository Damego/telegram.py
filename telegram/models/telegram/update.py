from attrs import define, field

from .message import Message
from ..attrs_utils import ClientSerializerMixin, convert_dataclass


@define(eq=False, order=False, hash=False, kw_only=True)
class Update(ClientSerializerMixin):
    update_id: int
    message: Message | None = field(converter=convert_dataclass(Message), default=None)
    edited_message: Message | None = field(converter=convert_dataclass(Message), default=None)
    channel_post: Message | None = field(converter=convert_dataclass(Message), default=None)
    edited_channel_post: Message | None = field(converter=convert_dataclass(Message), default=None)
    # inline_query
    # chosen_inline_result
    # callback_query
    # shipping_query
    # pre_checkout_query
    # poll
    # poll_answer
    # my_chat_member
    # chat_member
    # chat_join_request

