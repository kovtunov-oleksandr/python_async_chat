import asyncio
from utils.logger import logger
from utils.protocol.message import Message
from utils.protocol.connection import Connection


class Server:

    def __init__(self, host: str = 'localhost', port: int = 5050):
        self.host = host
        self.port = port
        self.__command_handler_map = {}

    async def run_server(self):
        server = await asyncio.start_server(self._handle_connection, self.host, self.port)
        logger.info(f'Server started on {self.host}:{self.port}')
        async with server:
            await server.serve_forever()

    async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        connection = Connection(writer, reader)
        async for message in connection.start_reading():
            await self._get_handler(message, connection)

    async def _get_handler(self, message: Message, connection: Connection):
        await self.__command_handler_map[message.command](message, connection)

    def message_handler(self, method: str):
        def decorator(func):
            self.__command_handler_map[method] = func
        return decorator
