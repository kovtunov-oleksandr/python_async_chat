from utils.protocol import Client, Message
import json


class ChatClient(Client):
    async def sign_up(self, data: dict):
        request = Message("sign_up", "client", "server", "_", json.dumps(data))
        await self.send_message(request)
