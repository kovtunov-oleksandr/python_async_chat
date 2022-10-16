from server.config.config import server


@server.add_handler('02')
async def sign_in():
    print('SIGN IN METHOD')