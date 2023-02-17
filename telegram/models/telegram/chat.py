from attrs import define

from ..attrs_utils import DictSerializerMixin


@define(kw_only=True)
class Chat(DictSerializerMixin):
    id: int
    type: str
    title: str
    username: str
    first_name: str
    last_name: str
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
