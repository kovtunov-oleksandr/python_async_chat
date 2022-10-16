from server.config.config import server
from utils.protocol.request import Request
from utils.protocol.connection import Connection
from utils.protocol.timestamp import form_timestamp


# 04;;1;;login(sender);;login(RECEIVER);;_;;msg;;TIME # private to: receiver:msg
# 04;;2;;login(sender);;login(RECEIVER);;_;;msg;;TIME # private from: sender:msg
# 04;;0;;login(sender);;login(RECEIVER);;_;;msg;;TIME # user not online
@server.add_handler('04')
async def send_private_message(request: Request):
    if server.sessions.get(request.receiver) is not None:
        response_to_sender = Request(f'04', '1', request.sender, request.receiver, '_', request.content, form_timestamp())
        server.sessions.get(response_to_sender.sender).send(response_to_sender.form_protocol())
        response_to_receiver = Request(f'04', '2', request.sender, request.receiver, '_', request.content, form_timestamp())
        server.sessions.get(response_to_receiver.sender).send(response_to_receiver.form_protocol())
    else:
        response = Request(f'04', '0', request.sender, request.receiver, '_', request.content, form_timestamp())
        server.sessions.get(response.sender).send(response.form_protocol())

