from server.config.config import server


@server.add_handler('01')
async def sign_up():
    print('SIGN UP METHOD')