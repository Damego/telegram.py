from datetime import datetime
from typing import Optional

from attrs import define, field

from .user import User
from ..attrs_utils import convert_dataclass, DictSerializerMixin
from .chat import Chat


@define(kw_only=True)
class Message(DictSerializerMixin):
    id: int
    user: Optional[User] = field(converter=convert_dataclass(User), default=None)
    chat: Chat = field(converter=convert_dataclass(Chat))
    date: datetime = field(converter=datetime.fromtimestamp)
    text: str

    @classmethod
    def process_dict(cls, data: dict) -> dict:
        data["id"] = data.pop("message_id")

        if "from" in data:
            data["user"] = data.pop("from")

        return data