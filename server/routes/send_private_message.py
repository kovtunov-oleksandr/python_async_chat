from server.config.config import server


@server.add_handler('04')
async def send_private_message():
    print('PRIVATE MESSAGE')