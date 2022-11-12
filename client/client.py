from utils.protocol import Client, Message


class ChatClient(Client):
    async def sign_up(self, data: dict):
        message = Message(
            "sign_up", "client", "server", "_", Message.decode_content_to_json(data)
        )
        return await self.send_message(message)

    async def sign_in(self, data: dict):
        message = Message(
            "sign_in", "client", "server", "_", Message.decode_content_to_json(data)
        )
        return await self.send_message(message)

    async def create_chat(self, data: dict):
        data["user_id"] = self.user_id
        message = Message(
            "create_chat",
            "client",
            "server",
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def join_to_chat(self, data: dict):
        data["user_id"] = self.user_id
        message = Message(
            "join_to_group_chat",
            "client",
            "server",
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def get_group_members(self, data: dict):
        message = Message(
            "get_group_members",
            "client",
            "server",
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def get_all_groups(self, data: dict):
        data["user_id"] = self.user_id
        message = Message(
            "get_all_groups",
            "client",
            "server",
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def send_message_to_chat(self, data: dict):
        data["user_id"], data["nickname"] = self.user_id, self.nickname
        message = Message(
            "send_message_to_chat",
            "client",
            "server",
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)
