from sqlalchemy.future import select
import pytest
import pytest_asyncio
from server.models import Chat, ChatMember
from global_enums import CreateChat, Protocol
from utils.protocol import Message


@pytest.mark.asyncio
class TestCreateChat:

    async def test_successful_create_group_chat(self, sign_in, generate_chat_name, session):
        creator = sign_in
        chat_name = generate_chat_name
        data = {"creator_id": creator.user_id, "chat_name": chat_name, "type": CreateChat.PUBLIC.value}
        response: Message = await creator.create_chat(data)
        content = response.encode_content_from_json()
        assert response.command == CreateChat.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == CreateChat.RESPONSE_CHAT_CREATED.value
        chat = await session.scalar(select(Chat).where(Chat.chat_name == chat_name))
        chat_member = await session.sceler(select(ChatMember).where(ChatMember.chat_id == chat.id, ChatMember.user_id == creator.user_id))
        assert chat is not None
        assert chat_member is not None


    def test_successful_create_private_chat(self):
        assert True

    def test_failed_create_chat_name_exists(self):
        assert True

    def test_failed_create_chat_second_user_missed(self):
        assert True

    def test_failed_create_chat_second_user_not_found(self):
        assert True
