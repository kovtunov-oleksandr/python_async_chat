import asyncio
from utils.protocol.message import Message


class Waiter:
    def __init__(self, command: str):
        self.command = command
        self.event = asyncio.Event()
        self._message = None

    @property
    def message(self) -> Message:
        return self._message

    @message.setter
    def message(self, message: Message):
        if self.event.is_set():
            raise RuntimeError("Message already set")
        self._message = message
        self.event.set()

    async def wait_message(self) -> Message:
        await self.event.wait()
        return self.message
