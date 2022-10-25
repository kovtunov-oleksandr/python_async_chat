from utils.protocol.client import Client
from utils.protocol.message import Message


class ChatClient(Client):

    def sign_in(self, message: Message):
        self.send_message(message)
