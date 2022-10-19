import asyncio
from utils.protocol import Message, Connection
from server.config import HOST, PORT, DATA_CODING_FORMAT


class Client:
    def __init__(self):
        self.session = {"user": "", "token": ""}
        self.host = HOST
        self.port = PORT
        self.connection = Connection()

    async def send(self, data: str):
        self.connection.writer.write(data.encode(DATA_CODING_FORMAT))
        await self.connection.drain()

    async def listen_incoming(self):
        while True:
            data = await self.connection.reader.read(1024)
            response = data.decode(DATA_CODING_FORMAT)
            if not response:
                raise Exception("Connection closed")
            return response

    async def start_client(self):
        await asyncio.create_task(self.listen_incoming())
