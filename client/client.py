from utils.protocol import Client
from utils.protocol.message import Message
import json


class ChatClient(Client):
    async def create_chat(self, data: dict):
        message = Message("create_chat", "client", "server", "_", json.dumps(data))
        await self.send_message(message)
