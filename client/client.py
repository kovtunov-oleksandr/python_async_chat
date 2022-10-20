import asyncio
from utils.protocol.connection import Connection
from utils.protocol.message import Message


class Client:
    def __init__(self, host, port):
        self.session = {"user": "", "token": ""}
        self.host = host
        self.port = port

    async def connect(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.connection = Connection(writer, reader)

    async def read_messages(self):
        async for message in self.connection.start_reading():
            print(message)

    async def send_messages(self, message):
        await self.connection.send_message_wait_answer(message)

    async def quick_start(self):
        await self.connect()
        write = asyncio.create_task(
            self.send_messages(
                Message(
                    "sign_in", "sender", "receiver", "token", "content"
                )  # change to
            )
        )
        await asyncio.create_task(self.read_messages())


if __name__ == "__main__":
    client = Client("localhost", 5050)
    asyncio.run(client.quick_start())
