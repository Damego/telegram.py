from enum import Enum

from attrs import field

from ..attrs_utils import define, DictSerializerMixin


@define()
class BotCommand(DictSerializerMixin):
    command: str
    description: str


class BotCommandScopeType(str, Enum):
    DEFAULT = "default"
    ALL_PRIVATE_CHATS = "all_private_chats"
    ALL_GROUP_CHATS = "all_group_chats"
    ALL_CHAT_ADMINISTRATORS = "all_chat_administrators"
    CHAT = "chat"
    CHAT_ADMINISTRATORS = "chat_administrators"
    CHAT_MEMBER = "chat_member"


@define()
class BotCommandScope(DictSerializerMixin):
    type: BotCommandScopeType = field()


@define()
class BotCommandScopeDefault(BotCommandScope):
    type: BotCommandScopeType = field(default=BotCommandScopeType.DEFAULT)


@define()
class BotCommandScopeAllPrivateChats(BotCommandScope):
    type: BotCommandScopeType = field(default=BotCommandScopeType.ALL_PRIVATE_CHATS)


@define()
class BotCommandScopeAllGroupChats(BotCommandScope):
    type: BotCommandScopeType = field(default=BotCommandScopeType.ALL_GROUP_CHATS)


@define()
class BotCommandScopeAllChatAdministrators(BotCommandScope):
    type: BotCommandScopeType = field(default=BotCommandScopeType.ALL_CHAT_ADMINISTRATORS)


@define()
class BotCommandScopeChat(BotCommandScope):
    type: BotCommandScopeType = field(default=BotCommandScopeType.CHAT)
    chat_id: int | str = field()


@define()
class BotCommandScopeChatAdministrators(BotCommandScope):
    type: BotCommandScopeType = field(default=BotCommandScopeType.CHAT_ADMINISTRATORS)
    chat_id: int | str = field()


@define()
class BotCommandScopeChatMember(BotCommandScope):
    type: BotCommandScopeType = field(default=BotCommandScopeType.CHAT_MEMBER)
    chat_id: int | str = field()
    user_id: int = field()
