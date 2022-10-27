import json
from utils.protocol.client import Client
from utils.protocol.message import Message


class ChatClient(Client):

    def sign_in(self, data: dict):
        message = Message("sign_in", "_", "server", "_", json.dumps(data))
        self.send_message(message)
