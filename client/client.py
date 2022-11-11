from utils.protocol import Client, Message


class ChatClient(Client):
    async def sign_up(self, data: dict):
        message = Message(
            "sign_up", "client", "server", "_", Message.decode_content_to_json(data)
        )
        await self.send_message(message)

    async def sign_in(self, data: dict):
        message = Message(
            "sign_in", "client", "server", "_", Message.decode_content_to_json(data)
        )
        await self.send_message(message)

    async def create_chat(self, data: dict):
        data["user_id"] = self.user_id
        message = Message(
            "create_chat",
            "client",
            "server",
            self.token,
            Message.decode_content_to_json(data),
        )
        await self.send_message(message)

    async def join_to_chat(self, data: dict):
        data["user_id"] = self.user_id
        message = Message(
            "join_to_group_chat",
            "client",
            "server",
            self.token,
            Message.decode_content_to_json(data),
        )
        await self.send_message(message)

    async def get_group_members(self, data: dict):
        message = Message(
            "get_group_members",
            "client",
            "server",
            self.token,
            Message.decode_content_to_json(data),
        )
        await self.send_message(message)

    async def leave_chat(self, data: dict):
        message = Message(
            "leave_chat",
            "client",
            "server",
            self.token,
            Message.decode_content_to_json(data),
        )
        await self.send_message(message)
