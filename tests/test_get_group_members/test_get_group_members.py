from sqlalchemy.future import select
import pytest
from server.models import Chat, ChatMember
from global_enums import CreateChat, Protocol, GetMembers
from utils.protocol.message import Message


@pytest.mark.asyncio
class TestGetGroupMembers:
    async def test_successful_get_group_members(self, create_user_session, generate_chat_id):
        client = create_user_session
        chat_id = generate_chat_id
        response, content = await self.send_message(
            client, (chat_id)
        )
        assert response.command == GetMembers.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == GetMembers.RESPONSE_LIST_RETRIEVED.value


    async def send_message(self, client, data: tuple) -> tuple:
        chat_id = data
        data = {"chat_id": chat_id, "user_id": client.user_id}
        response: Message = await client.get_group_members(data)
        content = response.encode_content_from_json()
        return response, content
