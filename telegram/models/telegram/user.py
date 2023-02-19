from attrs import field
from typing import Literal

from ..attrs_utils import ClientSerializerMixin, define


@define()
class User(ClientSerializerMixin):
    id: int
    is_bot: bool
    first_name: str
    last_name: str | None = field(default=None)
    username: str | None = field(default=None)
    language_code: str | None = field(default=None)
    is_premium: Literal[True] | None = field(default=None)
    added_to_attachment_menu: Literal[True] | None = field(default=None)
    can_join_groups: bool | None = field(default=None)
    can_read_all_group_messages: bool | None = field(default=None)
    supports_inline_queries: bool | None = field(default=None)
