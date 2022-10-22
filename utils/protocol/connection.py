import asyncio
from utils.logger import logger
from utils.protocol.message import Message
from utils.protocol.waiter import Waiter


class Connection:

    DATA_CODING_FORMAT = "utf-8"

    def __init__(self, writer: asyncio.StreamWriter, reader: asyncio.StreamReader):
        self.writer = writer
        self.reader = reader
        self.waiters = {}
        extra_info = self.writer.get_extra_info("peername")
        self.remote_host = extra_info[0] + ":" + str(extra_info[1])

    async def create_message_waiter(self, command: str) -> Waiter:
        waiter = Waiter(command)
        self.waiters[command] = waiter
        return waiter

    async def send_message(self, message: Message):
        logger.debug(f"OUT: {self.remote_host} data:{message}")
        self.writer.write(message.form_protocol().encode(self.DATA_CODING_FORMAT))
        await self.writer.drain()

    async def send_message_wait_answer(
        self, message: Message, answer_command: str = None
    ):
        if answer_command is None:
            answer_command = message.command
        waiter = await self.create_message_waiter(answer_command)
        await self.send_message(message)
        return await waiter.wait_message()

    async def read_message(self) -> Message:
        data = await self.reader.read(1024)
        if not data:
            raise ConnectionError("Connection closed")
        message: Message = Message.parse_protocol_message(data.decode(self.DATA_CODING_FORMAT))
        logger.debug(f"IN: {self.remote_host}: {message}")
        return message

    async def start_reading(self):
        while True:
            message = await self.read_message()
            if message.command in self.waiters:
                self.waiters[message.command].message = message
            yield message
