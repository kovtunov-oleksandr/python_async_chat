import asyncio
from utils.logger import logger
from utils.protocol.message import Message
from utils.protocol.connection import Connection
from utils.protocol.data_converters import parse_protocol_message


class Server:

    def __init__(self, host: str = 'localhost', port: int = 5050, data_coding_format='utf-8'):
        self.host = host
        self.port = port
        self.data_coding_format = data_coding_format
        self.__command_handler_map = {}

    async def run_server(self):
        server = await asyncio.start_server(self._handle_connection, self.host, self.port)
        logger.info(f'Server started on {self.host}:{self.port}')
        async with server:
            await server.serve_forever()

    async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        while True:
            data = await reader.read(1024)
            logger.debug(f'IN: {writer.get_extra_info("peername")} data: {data}')
            connection = Connection(writer, reader)
            message: Message = parse_protocol_message(data.decode(self.data_coding_format))
            logger.debug(f'Data decoded: {message.form_protocol()}')
            await self._get_handler(message, connection)

    async def _get_handler(self, message: Message, connection: Connection):
        await self.__command_handler_map[message.command](message, connection)

    def message_handler(self, method: str):
        def decorator(func):
            self.__command_handler_map[method] = func
        return decorator
