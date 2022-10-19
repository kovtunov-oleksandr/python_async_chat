from server.config import server
from utils.protocol.message import Message


@server.add_handler('sign_up')
async def sign_up(request: Message):
    print('SIGN UP METHOD')
