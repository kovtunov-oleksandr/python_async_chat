import asyncio
from utils.protocol.connection import Connection
from utils.protocol.message import Message


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
        self.nickname = None
        self.user_id = None
        self.token = None

    async def connect(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.connection = Connection(writer, reader)

    async def read_messages(self):
        async for message in self.connection.start_reading():
            message

    async def send_message(self, message: Message):
        return await self.connection.send_message_wait_answer(message)

    async def quick_start(self):
        await self.connect()
        await asyncio.create_task(self.read_messages())

    async def disconnect(self):
        await self.connection.disconnect()
