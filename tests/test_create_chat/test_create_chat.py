from sqlalchemy.future import select
from tests.utils.generate_chat_name import generate_chat_name
import pytest
from server.models import Chat, ChatMember
from global_enums import CreateChat, Protocol
from utils.protocol.message import Message


@pytest.mark.asyncio
class TestCreateChat:
    async def test_successful_create_group_chat(self, create_user_session, session):
        client = create_user_session
        chat_name = generate_chat_name()
        response, content = await self.send_message(
            client, (chat_name, CreateChat.PUBLIC.value)
        )
        assert response.command == CreateChat.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == CreateChat.RESPONSE_CHAT_CREATED.value
        chat = await session.scalar(select(Chat).where(Chat.chat_name == chat_name))
        chat_member = await session.scalar(
            select(ChatMember).where(
                ChatMember.chat_id == chat.id, ChatMember.user_id == client.user_id
            )
        )
        assert chat is not None
        assert chat_member is not None

    async def test_successful_create_private_chat(
        self, create_user_session, generate_user_in_db, session
    ):
        client = create_user_session
        second_user = generate_user_in_db[1]
        chat_name = generate_chat_name()
        response, content = await self.send_message(
            client, (chat_name, CreateChat.PRIVATE.value, second_user.id)
        )
        assert response.command == CreateChat.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == CreateChat.RESPONSE_CHAT_CREATED.value
        chat_id = content.get("chat_id")
        chat_members = await session.scalars(
            select(ChatMember).where(ChatMember.chat_id == chat_id)
        )
        chat_members = chat_members.all()
        assert len(chat_members) == 2

    async def test_failed_create_chat_name_exists(
        self, create_user_session, generate_chat_in_db
    ):
        client = create_user_session
        chat_name = generate_chat_in_db.chat_name
        response, content = await self.send_message(
            client, (chat_name, CreateChat.PUBLIC.value)
        )
        assert response.command == CreateChat.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == CreateChat.RESPONSE_CHAT_NAME_EXISTS.value

    async def test_failed_create_chat_second_user_not_found(self, create_user_session):
        client = create_user_session
        second_user_id = -1
        chat_name = generate_chat_name()
        response, content = await self.send_message(
            client, (chat_name, CreateChat.PRIVATE.value, second_user_id)
        )
        assert response.command == CreateChat.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert (
            content.get("response") == CreateChat.RESPONSE_SECOND_USER_NOT_FOUND.value
        )

    async def send_message(self, client, info: tuple) -> tuple:
        chat_name, chat_type = info[0], info[1]
        data = {
            "user_id": client.user_id,
            "chat_name": chat_name,
            "chat_type": chat_type,
        }
        if len(info) == 3:
            data["second_user_id"] = info[-1]
        response: Message = await client.create_chat(data)
        content = response.encode_content_from_json()
        return response, content
