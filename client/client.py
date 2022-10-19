import asyncio
from utils.protocol import Message, Connection
from server.config import DATA_CODING_FORMAT
from utils.protocol.envs import LOCAL


host, port = LOCAL


class Client:
    def __init__(self, host, port):
        self.session = {"user": "", "token": ""}
        self.host = host
        self.port = port
        self.connection = Connection()

    async def send(self, data: str):
        await self.connection.send_message(data)

    async def listen_incoming(self):
        while True:
            data = await self.connection.reader.read(1024)
            response = data.decode(DATA_CODING_FORMAT)
            if not response:
                raise Exception("ConnectionError")
            return response

    async def start_client(self):
        await asyncio.create_task(self.listen_incoming())


#
