import asyncio
from utils.protocol.connection import Connection


class Client:
    connection: Connection

    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def connect(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.connection = Connection(writer, reader)
        asyncio.create_task(self.read_messages())

    async def read_messages(self):
        async for message in self.connection.start_reading():
            print(message)
