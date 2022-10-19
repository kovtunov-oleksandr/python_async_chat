from server.config import server
from utils.protocol.message import Message
from utils.protocol.connection import Connection


@server.message_handler('sign_up')
async def sign_up(request: Message, connection: Connection):
    print('SIGN UP METHOD')
