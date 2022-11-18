from global_enums import *
from utils.protocol import Client, Message


class ChatClient(Client):
    async def sign_up(self, data: dict):
        message = Message(
            SignUP.COMMAND.value,
            Protocol.CLIENT.value,
            Protocol.SERVER.value,
            Protocol.EMPTY_TOKEN.value,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def sign_in(self, data: dict):
        message = Message(
            SignIn.COMMAND.value,
            Protocol.CLIENT.value,
            Protocol.SERVER.value,
            Protocol.EMPTY_TOKEN.value,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def create_chat(self, data: dict):
        data["user_id"] = self.user_id
        message = Message(
            CreateChat.COMMAND.value,
            Protocol.CLIENT.value,
            Protocol.SERVER.value,
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def join_to_chat(self, data: dict):
        data["user_id"] = self.user_id
        message = Message(
            JoinGroup.COMMAND.value,
            Protocol.CLIENT.value,
            Protocol.SERVER.value,
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def get_group_members(self, data: dict):
        message = Message(
            GetMembers.COMMAND.value,
            Protocol.CLIENT.value,
            Protocol.SERVER.value,
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def get_all_groups(self, data: dict):
        data["user_id"] = self.user_id
        message = Message(
            GetGroups.COMMAND.value,
            Protocol.CLIENT.value,
            Protocol.SERVER.value,
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)

    async def leave_chat(self, data: dict):
        data["user_id"] = self.user_id
        message = Message(
            LeaveChat.COMMAND.value,
            Protocol.CLIENT.value,
            Protocol.SERVER.value,
            self.token,
            Message.decode_content_to_json(data),
        )
        await self.send_message(message)

    async def send_message_to_chat(self, data: dict):
        data["user_id"], data["nickname"] = self.user_id, self.nickname
        message = Message(
            SendMessageToChat.COMMAND.value,
            Protocol.CLIENT.value,
            Protocol.SERVER.value,
            self.token,
            Message.decode_content_to_json(data),
        )
        return await self.send_message(message)
