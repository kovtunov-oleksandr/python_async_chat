from utils.protocol import Client, Message


class ChatClient(Client):
    async def sign_up(self, data: dict):
        message = Message("sign_up", "client", "server", "_", Message.decode_content_to_json(data))
        await self.send_message(message)

    async def sign_in(self, data: dict):
        message = Message("sign_in", "client", "server", "_", Message.decode_content_to_json(data))
        await self.send_message(message)

    async def create_chat(self, data: dict):
        data["user_id"] = self.user_id
        message = Message("create_chat", "client", "server", self.token, Message.decode_content_to_json(data))
        await self.send_message(message)
