from attrs import define, field

from ..attrs_utils import DictSerializerMixin, convert_dataclass, convert_list_dataclass


@define(kw_only=True)
class KeyboardButtonRequestUser(DictSerializerMixin):
    request_id: int
    user_is_bot: bool | None = field(default=None)
    user_id_premium: bool | None = field(default=None)


@define(kw_only=True)
class KeyboardButtonRequestChat(DictSerializerMixin):
    request_id: int
    chat_is_channel: bool | None = field(default=None)
    chat_is_forum: bool | None = field(default=None)
    chat_has_username: bool | None = field(default=None)
    chat_is_created: bool | None = field(default=None)
    # user_administrator_rights
    # bot_administrator_rights
    bot_is_member: bool | None = field(default=None)


@define(kw_only=True)
class KeyboardButtonPollType(DictSerializerMixin):
    type: str | None = field(default=None)


@define(kw_only=True)
class KeyboardButton(DictSerializerMixin):
    text: str
    request_user: KeyboardButtonRequestUser | None = field(converter=convert_dataclass(KeyboardButtonRequestUser))
    request_chat: KeyboardButtonRequestChat | None = field(converter=convert_dataclass(KeyboardButtonRequestChat))
    request_contact: bool | None = field(default=None)
    request_location: bool | None = field(default=None)
    request_poll: KeyboardButtonPollType | None = field(converter=convert_dataclass(KeyboardButtonPollType))
    # web_app


@define(kw_only=True)
class ReplyKeyboardMarkup(DictSerializerMixin):
    keyboard: list[KeyboardButton] = field(converter=convert_list_dataclass(KeyboardButton))
    is_persistent: bool | None = field(default=None)
    resize_keyboard: bool | None = field(default=None)
    one_time_keyboard: bool | None = field(default=None)
    input_field_placeholder: str | None = field(default=None)
    selective: bool | None = field(default=None)


@define(kw_only=True)
class ReplyKeyboardRemove(DictSerializerMixin):
    remove_keyboard: bool | None = field(default=None)
    selective: bool | None = field(default=None)


@define(kw_only=True)
class InlineKeyboardButton(DictSerializerMixin):
    text: str
    url: str | None = field(default=None)
    callback_data: str | None = field(default=None)
    # web_app
    # login_url
    switch_inline_query: str | None = field(default=None)
    switch_inline_query_current_chat: str | None = field(default=None)
    # callback_game
    pay: bool | None = field(default=None)


@define(kw_only=True)
class InlineKeyboardMarkup(DictSerializerMixin):
    inline_keyboard: list[list[InlineKeyboardButton]] = field()

    def __attrs_post_init__(self):
        self.inline_keyboard = [
            [
                InlineKeyboardButton.from_dict(data)
                for data in row
            ]
            for row in self.inline_keyboard
        ]


@define(kw_only=True)
class LoginUrl(DictSerializerMixin):
    url: str
    forward_text: str | None = field(default=None)
    bot_username: str | None = field(default=None)
    request_write_access: bool | None = field(default=None)
