from sqlalchemy.future import select
import pytest
from server.models import ChatMember
from global_enums import JoinGroup, Protocol
from utils.protocol.message import Message


@pytest.mark.asyncio
class TestJoinToGroupChat:
    async def test_successful_join(
        self, create_user_session, generate_chat_in_db, session
    ):
        client = create_user_session
        chat = generate_chat_in_db
        response, content = await self.send_message(client, chat.id)
        assert response.command == JoinGroup.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == JoinGroup.RESPONSE_CHAT_JOINED.value
        chat_member = await session.scalar(
            select(ChatMember).where(
                ChatMember.chat_id == chat.id, ChatMember.user_id == client.user_id
            )
        )
        assert chat_member

    async def test_failed_join_chat_not_found(self, create_user_session, generate_non_exist_chat_id):
        client = create_user_session
        chat_id = generate_non_exist_chat_id
        response, content = await self.send_message(client, chat_id)
        assert response.command == JoinGroup.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == JoinGroup.RESPONSE_CHAT_NOT_FOUND.value

    async def test_failed_join_user_already_in_chat(
        self, create_user_session, generate_chat_in_db, generate_chat_member
    ):
        client = create_user_session
        chat = generate_chat_in_db
        response, content = await self.send_message(client, chat.id)
        assert response.command == JoinGroup.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == JoinGroup.RESPONSE_ALREADY_IN_CHAT.value

    async def send_message(self, client, chat_id: int) -> tuple:
        data = {"chat_id": chat_id, "user_id": client.user_id}
        response: Message = await client.join_to_group_chat(data)
        content = response.encode_content_from_json()
        return response, content
