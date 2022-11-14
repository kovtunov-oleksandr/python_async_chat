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
            # await asyncio.sleep(0.1)
            self.answer_handler(message)

    async def send_message(self, message: Message):
        return await self.connection.send_message_wait_answer(message)

    async def quick_start(self):
        await self.connect()
        await asyncio.create_task(self.read_messages())

    async def disconnect(self):
        await self.connection.disconnect()

    def answer_handler(self, message: Message):
        content = message.encode_content_from_json()
        if (
                message.command == "sign_in"
                and content.get("response") == "SUCCESSFULLY LOGGED IN"

        ):
            self.token = message.token
            self.nickname = content.get("nickname")
            self.user_id = content.get("user_id")

        return message
