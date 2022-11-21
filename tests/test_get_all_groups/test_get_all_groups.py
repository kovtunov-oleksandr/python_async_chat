import pytest
from global_enums import Protocol, GetGroups
from utils.protocol.message import Message


@pytest.mark.asyncio
class TestGetGroupMembers:
    async def test_successful_get_all_groups(self, create_user_session, generate_chats_in_db):
        client = create_user_session
        response, content = await self.send_message(client)
        assert response.command == GetGroups.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == GetGroups.RESPONSE_LIST_RETRIEVED.value

    async def test_chat_not_found(self, create_user_session):
        client = create_user_session
        response, content = await self.send_message(client)
        assert response.command == GetGroups.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == GetGroups.RESPONSE_CHAT_NOT_FOUND.value

    async def send_message(self, client) -> tuple:
        data = {"user_id": client.user_id}
        response: Message = await client.get_all_groups(data)
        content = response.encode_content_from_json()
        return response, content
