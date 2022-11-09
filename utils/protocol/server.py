import asyncio
from utils.logger import logger
from utils.protocol import Message, Connection


class Server:
    def __init__(self, host: str = "localhost", port: int = 5050):
        self.host = host
        self.port = port
        self.sessions = {}
        self.__command_handler_map = {}

    async def run_server(self):
        server = await asyncio.start_server(self._handle_connection, self.host, self.port)
        logger.info(f"Server started on {self.host}:{self.port}")
        async with server:
            await server.serve_forever()

    async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        connection = Connection(writer, reader)
        async for message in connection.start_reading():
            await self._get_handler(message, connection)

    async def _get_handler(self, message: Message, connection: Connection):
        if await self.check_user_session(message, connection):
            await self.__command_handler_map[message.command](message, connection)

    def message_handler(self, method: str):
        def decorator(func):
            self.__command_handler_map[method] = func

        return decorator

    async def check_user_session(self, message: Message, connection: Connection) -> bool:
        if message.command not in ["sign_up", "sign_in"]:
            logger.info("Checking user token auth")
            content = message.encode_content_from_json()
            user_id = content.get("user_id")
            if user_id not in self.sessions:
                response = {"response": "ERROR: NO SUCH USER SESSION"}
                await connection.send_message(
                    Message(message.command, "server", "client", "_", Message.decode_content_to_json(response))
                )
                return False
            user_session = self.sessions.get(user_id).get("user_session")
            if user_session.token != message.token:
                response = {"response": "USER SESSION ERROR: TOKEN AUTH FAIL"}
                await connection.send_message(
                    Message(message.command, "server", "client", "_", Message.decode_content_to_json(response))
                )
                return False
        logger.info("Token auth check successful")
        return True

    @property
    def command_handler_map(self):
        return self.__command_handler_map
