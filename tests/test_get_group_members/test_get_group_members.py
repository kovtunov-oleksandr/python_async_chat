import pytest
from global_enums import Protocol, GetMembers
from utils.protocol.message import Message


@pytest.mark.asyncio
class TestGetGroupMembers:
    async def test_successful_get_group_members(self, create_user_session, generate_chatmember_in_db):
        client = create_user_session
        chatmember = generate_chatmember_in_db[0]
        chat_id = chatmember.chat_id
        response, content = await self.send_message(client, chat_id)
        assert response.command == GetMembers.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == GetMembers.RESPONSE_LIST_RETRIEVED.value

    async def test_chat_not_found(self, create_user_session, generate_chat_id):
        client = create_user_session
        chat_id = generate_chat_id
        response, content = await self.send_message(client, chat_id)
        assert response.command == GetMembers.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == GetMembers.RESPONSE_CHAT_NOT_FOUND.value + " " + str(generate_chat_id)

    async def send_message(self, client, data: tuple) -> tuple:
        chat_id = data
        data = {"chat_id": chat_id, "user_id": client.user_id}
        response: Message = await client.get_group_members(data)
        content = response.encode_content_from_json()
        return response, content
