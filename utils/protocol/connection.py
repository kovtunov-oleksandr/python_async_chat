import asyncio
from utils.logger import logger
from utils.protocol.data_converters import parse_protocol_message
from utils.protocol.message import Message
from utils.protocol.waiter import Waiter


class Connection:
    def __init__(self, writer: asyncio.StreamWriter, reader: asyncio.StreamReader):
        self.writer = writer
        self.reader = reader
        self.waiters = {}
        extra_info = self.writer.get_extra_info("peername")
        self.remote_host = extra_info[0] + ":" + str(extra_info[1])

    async def create_message_waiter(self, command: str):
        waiter = Waiter(command)
        self.waiters[command] = waiter
        return waiter

    async def send_message(self, message: Message):
        logger.debug(f"OUT: {self.remote_host} data:{message}")
        self.writer.write(message.form_protocol().encode("utf-8"))
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
        message: Message = parse_protocol_message(data.decode("utf-8"))
        logger.debug(f"IN: {self.remote_host}: {message}")
        return message

    async def start_reading(self):
        while True:
            message = await self.read_message()
            if message.command in self.waiters:
                self.waiters[message.command].message = message
            yield message
