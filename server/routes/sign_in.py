from server.config import server
from utils.protocol.message import Message


@server.add_handler('02')
async def sign_in(request: Message):
    print('SIGN IN METHOD')