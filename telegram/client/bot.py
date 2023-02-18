import asyncio
from typing import Callable, Coroutine

from ..http.client import HTTPClient
from .polling import Polling
from .dispatch import Dispatch

from ..models.telegram import Update


class Bot:
    def __init__(self, token: str):
        self._http = HTTPClient(token)
        self._polling = Polling(self._http)
        self._dispatch = Dispatch()

        try:
            self._loop = asyncio.get_running_loop()
        except RuntimeError:
            self._loop = asyncio.new_event_loop()

    async def _start_polling(self):
        async for update in self._polling.polling():
            self._dispatch_handlers(update)

    # TODO: Resolve duplicate code

    def _dispatch_handlers(self, update: Update):
        if update.message:
            self._dispatch.dispatch("message", update.message)
        if update.edited_message:
            self._dispatch.dispatch("edited_message", update.edited_message)
        if update.callback_query:
            self._dispatch.dispatch("callback_query", update.callback_query)

    def on_message(self):
        def decorator(func: Callable[..., Coroutine]):
            self._dispatch.register(func, "message")
            return func
        return decorator

    def on_message_edit(self):
        def decorator(func: Callable[..., Coroutine]):
            self._dispatch.register(func, "edited_message")
            return func
        return decorator

    def on_callback_query(self):
        def decorator(func: Callable[..., Coroutine]):
            self._dispatch.register(func, "callback_query")
            return func
        return decorator

    def run(self):
        try:
            self._loop.run_until_complete(
                self._start_polling()
            )
        except KeyboardInterrupt:
            ...
