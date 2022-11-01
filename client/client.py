import asyncio
from utils.protocol import Client, Message
import json


class ChatClient(Client):
    async def sign_in(self, data: dict):
        message = Message("sign_in", "_", "server", "_", json.dumps(data))
        self.nickname = data["nickname"]
        await asyncio.create_task(self.send_message(message))

    async def read(self):
        await asyncio.create_task(self.read_messages())

    async def sign_up(self, data: dict):
        request = Message("sign_up", "client", "server", "_", json.dumps(data))
        await asyncio.create_task(self.send_message(request))

    async def create_chat(self, data: dict):
        message = Message(
            "create_chat", self.nickname, "server", self.session, json.dumps(data)
        )
        await asyncio.create_task(self.send_message(message))

    async def send_message_to_group_chat(self, data: dict):
        message = Message(
            "send_message_to_group_chat",
            self.nickname,
            "server",
            self.session,
            json.dumps(data),
        )
        await asyncio.create_task(self.send_message(message))


if __name__ == "__main__":
    client = ChatClient("localhost", 5050)
