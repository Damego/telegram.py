from typing import Callable, Coroutine

from ...models.attrs_utils import define, field, DictSerializerMixin
from ...models.telegram import BotCommand


@define(kw_only=True)
class Command(DictSerializerMixin):
    metadata: BotCommand = field()
    coro: Callable[..., Coroutine] = field()

