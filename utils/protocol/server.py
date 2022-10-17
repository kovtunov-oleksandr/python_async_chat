import asyncio
import logging
import sys
from utils.protocol.message import Message
from utils.protocol.connection import Connection
from utils.protocol.data_converters import parse_protocol_message

logging.basicConfig(stream=sys.stderr, level=logging.NOTSET,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Server:

    DATA_CODING_FORMAT = "utf-8"

    def __init__(self, host: str = 'localhost', port: int = 5050):
        self.host = host
        self.port = port
        self.sessions = {}
        self.command_handler_map = {}

    async def run_server(self):
        server = await asyncio.start_server(self.handle_connection, self.host, self.port)
        logger.info(f'Server started on {self.host}:{self.port}')
        logger.info(f'Command handle map is formed: {self.command_handler_map}')
        async with server:
            await server.serve_forever()

    async def handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """ Data protocol: command;;status_code;;sender;;receiver;;auth;;content;;time """
        while True:
            data = await reader.read(1024)
            logger.debug(f'Received from {writer.get_extra_info("peername")} data: {data}')
            connection = Connection(writer)
            message: Message = parse_protocol_message(data.decode(self.DATA_CODING_FORMAT))
            logger.debug(f'Data decoded: {message.form_protocol()}')
            await self.command_handler_map.get(message.command)(message)

    def add_handler(self, method: str):
        def inner(func):
            logger.info(f'Handler collector has started, new handler found: {func.__name__}')
            self.command_handler_map[method] = func
        return inner
