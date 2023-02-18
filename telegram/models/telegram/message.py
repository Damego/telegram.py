from datetime import datetime
from typing import Literal, Optional

from attrs import define, field

from .user import User
from ..attrs_utils import ClientSerializerMixin, DictSerializerMixin, convert, convert_dataclass, convert_list_dataclass
from .chat import Chat
from ...utils.types import MISSING, Absent
from .keyboard import ReplyKeyboardMarkup, InlineKeyboardMarkup


@define(kw_only=True)
class MessageEntity(DictSerializerMixin):
    type: str
    offset: int
    length: int
    url: str | None = field(default=None)
    user: User | None = field(converter=convert_dataclass(User), default=None)
    language: str | None = field(default=None)
    custom_emoji_id: str | None = field(default=None)


@define(kw_only=True)
class Message(ClientSerializerMixin):
    id: int
    message_thread_id: int | None = field(default=None)
    user: User | None = field(converter=convert_dataclass(User), default=None)  # from
    sender_chat: Chat = field(converter=convert_dataclass(Chat), default=None)
    date: datetime = field(converter=datetime.fromtimestamp)
    chat: Chat = field(converter=convert_dataclass(Chat))
    forward_user: User | None = field(converter=convert_dataclass(User), default=None)  # forward_from
    forward_from_chat: Chat | None = field(converter=convert_dataclass(Chat), default=None)
    forward_from_message_id: int | None = field(default=None)
    forward_signature: str | None = field(default=None)
    forward_sender_name: str | None = field(default=None)
    forward_date: datetime | None = field(converter=convert(datetime.fromtimestamp), default=None)
    is_topic_message: Literal[True] | None = field(default=None)
    is_automatic_forward: Literal[True] | None = field(default=None)
    reply_to_message: Optional["Message"] = field(default=None)
    via_bot: User | None = field(converter=convert_dataclass(User), default=None)
    edit_date: datetime | None = field(converter=convert(datetime.fromtimestamp), default=None)
    has_protected_content: Literal[True] | None = field(default=None)
    media_group_id: str | None = field(default=None)
    author_signature: str | None = field(default=None)
    text: str | None = field(default=None)
    entities: list[MessageEntity] | None = field(converter=convert_list_dataclass(MessageEntity), default=None)
    # animation
    # audio
    # document
    # photo
    # sticker
    # video
    # video_note
    # voice
    # caption: str | None = field(default=None)
    # caption_entities
    # has_media_spoiler: Literal[True] | None = field(default=None)
    # contact
    # dice
    # game
    # poll
    # venue
    # location
    # new_chat_members: list[User] | None = field(converter=convert_list_dataclass(User), default=None)
    # left_chat_member: User | None = field(converter=convert_dataclass(User), default=None)
    # new_chat_title: str | None = field(default=None)
    # new_chat_photo
    # delete_chat_photo: Literal[True] | None = field(default=None)
    # group_chat_created: Literal[True] | None = field(default=None)
    # supergroup_chat_created: Literal[True] | None = field(default=None)
    # channel_chat_created: Literal[True] | None = field(default=None)
    # message_auto_delete_timer_changed
    # migrate_to_chat_id: int | None = field(default=None)
    # migrate_from_chat_id: int | None = field(default=None)
    # pinned_message: Optional["Message"] = field(default=None)
    # invoice
    # successful_payment
    # user_shared
    # chat_shared
    # connected_website: str | None = field(default=None)
    # write_access_allowed
    # passport_data
    # proximity_alert_triggered
    # forum_topic_created
    # forum_topic_edited
    # forum_topic_closed
    # forum_topic_reopened
    # general_forum_topic_hidden
    # general_forum_topic_unhidden
    # video_chat_scheduled
    # video_chat_started
    # video_chat_ended
    # video_chat_participants_invited
    # web_app_data
    reply_markup: InlineKeyboardMarkup | None = field(converter=convert_dataclass(InlineKeyboardMarkup), default=None)

    @classmethod
    def process_dict(cls, data: dict, http) -> dict:
        if "message_id" in data:
            data["id"] = data.pop("message_id")
        if "from" in data:
            data["user"] = data.pop("from")
        if "forward_from" in data:
            data["forward_user"] = data.pop("forward_from")

        return super().process_dict(data, http)

    @property
    def author(self) -> User:
        return self.user

    async def reply_text(
        self,
        text: str,
        message_thread_id: Absent[int] = MISSING,
        parse_mode: Absent[str] = MISSING,
        entities: Absent[list[dict]] = MISSING,
        disable_web_page_preview: Absent[bool] = MISSING,
        disable_notification: Absent[bool] = MISSING,
        protect_content: Absent[bool] = MISSING,
        allow_sending_without_reply: Absent[bool] = MISSING,
        reply_markup: Absent[ReplyKeyboardMarkup] = MISSING,
    ) -> "Message":
        payload = {}
        if message_thread_id is not MISSING:
            payload["message_thread_id"] = message_thread_id
        if parse_mode is not MISSING:
            payload["parse_mode"] = parse_mode
        if entities is not MISSING:
            payload["entities"] = entities
        if disable_web_page_preview is not MISSING:
            payload["disable_web_page_preview"] = disable_web_page_preview
        if disable_notification is not MISSING:
            payload["disable_notification"] = disable_notification
        if protect_content is not MISSING:
            payload["protect_content"] = protect_content
        if allow_sending_without_reply is not MISSING:
            payload["allow_sending_without_reply"] = allow_sending_without_reply
        if reply_markup is not MISSING:
            payload["reply_markup"] = reply_markup.to_dict()

        response = await self.http.send_message(
            self.chat.id,
            text,
            reply_to_message_id=self.id,
            **payload
        )

        return Message.from_dict(response, self.http)
