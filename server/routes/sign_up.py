from server.config.config import server
from utils.protocol.request import Request
from utils.protocol.connection import Connection

@server.add_handler('01')
async def sign_up(request: Request):  # TODO: implement method when DB is up
    print('SIGN UP METHOD')