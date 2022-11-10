import asyncio
from utils.protocol.message import Message
from utils.protocol.connection import Connection


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.nickname = None
        self.token = None
        self.user_id = None
        self.connection = None

    async def connect(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.connection = Connection(writer, reader)

    async def read_messages(self):
        async for message in self.connection.start_reading():
            self.sign_in_answer_handler(message)

    async def send_message(self, message: Message):
        await self.connection.send_message_wait_answer(message)

    async def quick_start(self):
        await self.connect()
        await asyncio.create_task(self.read_messages())

    def sign_in_answer_handler(self, message: Message):
        content = message.encode_content_from_json()
        if (
                message.command == "sign_in"
                and content["response"] == "SUCCESSFULLY LOGGED IN"
        ):
            self.token = message.token
            self.nickname = content["nickname"]
            self.user_id = content["user_id"]
        return message
