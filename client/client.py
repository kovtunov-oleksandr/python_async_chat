import json
from utils.protocol.client import Client
from utils.protocol.message import Message


class ChatClient(Client):

    async def sign_in(self, data: dict):
        message = Message("sign_in", "_", "server", "_", Message.decode_content_to_json(data))
        await self.send_message(message)
