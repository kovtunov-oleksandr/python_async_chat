from server.config.config import server
from utils.protocol.request import Request
from utils.protocol.connection import Connection
from utils.protocol.timestamp import form_timestamp


# TODO: 03;;status_code;;login(sender);;CHAT_ID;;_;;msg;;TIME
@server.add_handler('03')
async def send_message_to_all(request: Request):
    response = Request(f'03', '1', request.sender, request.receiver, '_', request.content, form_timestamp())
    print(response)  # TODO: delete or log this
    for connection in server.sessions.values():
        connection.send(response.form_protocol())

