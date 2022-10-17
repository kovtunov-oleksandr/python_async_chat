from server.config import server
from utils.protocol.message import Message


@server.add_handler('01')
async def sign_up(request: Message):
    print('SIGN UP METHOD')