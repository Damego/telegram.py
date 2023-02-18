from attrs import define, field

from ..attrs_utils import DictSerializerMixin


@define(kw_only=True)
class Chat(DictSerializerMixin):
    id: int
    type: str
    title: str | None = field(default=None)
    username: str | None = field(default=None)
    first_name: str | None = field(default=None)
    last_name: str | None = field(default=None)
    # is_forum
    # photo
    # active_usernames
    # emoji_status_custom_emoji_id
    # bio
    # has_private_forwards
    # has_restricted_voice_and_video_messages
    # join_to_send_messages
    # join_by_request
    # description
    # invite_link
    # pinned_message
    # permissions
    # slow_mode_delay
    # message_auto_delete_time
    # has_aggressive_anti_spam_enabled
    # has_hidden_members
    # has_protected_content
    # sticker_set_name
    # can_set_sticker_set
    # linked_chat_id
    # location
