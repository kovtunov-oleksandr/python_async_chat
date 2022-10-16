from server.config.config import server
from utils.protocol.request import Request
from utils.protocol.connection import Connection


@server.add_handler('02')
async def sign_in(request: Request):  # TODO: implement method when DB is up
    print('SIGN IN METHOD')