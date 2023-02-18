from typing import Callable, Coroutine

from ..attrs_utils import define, field, DictSerializerMixin


@define(kw_only=True)
class BotCommand(DictSerializerMixin):
    command: str
    description: str


@define(kw_only=True)
class Command(DictSerializerMixin):
    metadata: BotCommand = field()
    coro: Callable[..., Coroutine] = field()