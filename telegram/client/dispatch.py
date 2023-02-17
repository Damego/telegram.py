import asyncio
from typing import Callable, Coroutine
from collections import defaultdict


class Dispatch:
    def __init__(self):
        self._handler_coroutines: dict[str, list[Callable[..., Coroutine]]] = defaultdict(list)

    def register(self, coro: Callable[..., Coroutine], handler_name: str):
        self._handler_coroutines[handler_name].append(coro)

    def dispatch(self, handler_name: str, *args, **kwargs):
        for coro in self._handler_coroutines.get(handler_name, []):
            asyncio.create_task(coro(*args, **kwargs))