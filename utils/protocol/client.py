import asyncio
from utils.protocol.connection import Connection
from utils.protocol.message import Message


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.session = []
        self.nickname = None
        self.connection = None

    async def connect(self):
        """When create Client instance create connection"""
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.connection = Connection(writer, reader)

    async def read_messages(self):
        async for message in self.connection.start_reading():
            self.answer_handler(message)

    async def send_message(self, message: Message):
        await self.connection.send_message_wait_answer(message)

    def answer_handler(self, message: Message):
        if (
            message.command == "sign_in"
            and message.content == '{"response": "SUCCESSFULLY LOGGED IN"}'
        ):
            self.session = message.token
        return message

    async def quick_start(self, message):
        await self.connect()
        await asyncio.create_task(self.send_message(message))
        await asyncio.create_task(self.read_messages())


if __name__ == "__main__":
    pass
