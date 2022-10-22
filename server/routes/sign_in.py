from server.config import server
from utils.protocol.message import Message
from utils.protocol.connection import Connection


@server.message_handler("sign_in")
async def sign_in(request: Message, connection: Connection):
    print("SIGN IN METHOD")
