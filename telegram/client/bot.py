import asyncio
from typing import Callable, Coroutine

from ..http.client import HTTPClient
from .polling import Polling
from .dispatch import Dispatch

from ..models.telegram import Update, Command, BotCommand, User


class Bot:
    def __init__(self, token: str):
        self._http = HTTPClient(token)
        self._polling = Polling(self._http)
        self._dispatch = Dispatch()

        self._commands: list[Command] = []

        try:
            self._loop = asyncio.get_running_loop()
        except RuntimeError:
            self._loop = asyncio.new_event_loop()

        self.user: User | None = None

    async def _run(self):
        self.user = User.from_dict(
            await self._http.get_me(),
            self._http
        )

        commands: list[dict] = [
            command.metadata.to_dict()
            for command in self._commands
        ]
        await self._http.set_my_commands(commands)

        self._dispatch.dispatch("startup")

        await self._start_polling()

    async def _start_polling(self):
        async for update in self._polling.polling():
            self._dispatch_handlers(update)

    def _dispatch_handlers(self, update: Update):
        known_handlers = {"message", "edited_message", "callback_query"}

        for handler_name in known_handlers:
            if (obj := getattr(update, handler_name, None)) is not None:
                self._dispatch.dispatch(handler_name, obj)

    def command(self, name: str | None = None, description: str = "No description set."):
        def decorator(coro: Callable[..., Coroutine]):
            command_name = name or coro.__name__

            self._commands.append(
                Command(
                    metadata=BotCommand(command=command_name, description=description),
                    coro=coro
                )
            )
            return coro
        return decorator

    def on_startup(self):
        def decorator(coro: Callable[..., Coroutine]):
            self._dispatch.register(coro, "startup")
            return coro
        return decorator

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
                self._run()
            )
        except KeyboardInterrupt:
            ...
