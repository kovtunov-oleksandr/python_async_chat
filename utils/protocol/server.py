import asyncio
from utils.protocol.request import Request
from utils.protocol.connection import Connection


class Server:

    def __init__(self, host, port, decode_format):
        self.HOST = host
        self.PORT = port
        self.FORMAT = decode_format
        self.sessions = {}  # TODO: {login: CONNECTION}
        self.command_map = {}

    async def run_server(self):
        server = await asyncio.start_server(self.handle_connection, self.HOST, self.PORT)
        async with server:
            await server.serve_forever()

    async def handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        while True:
            data = await reader.read(1024)  # TODO: command;;status_code;;sender;;receiver;;auth;;content;;time
            print(data)
            connection = Connection(writer, '_')
            request: Request = self.decode_protocol(data.decode(self.FORMAT))
            await self.command_map.get(request.command)(request)

    def add_handler(self, method):
        def inner(func):
            self.command_map[method] = func
        return inner

    def decode_protocol(self, data: str) -> Request:
        data = data.split(';;')
        request = Request(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        print(request)
        return request

