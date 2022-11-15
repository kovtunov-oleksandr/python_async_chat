import pytest
from global_enums import Session, GetGroups, Protocol

from utils.protocol import Message


@pytest.mark.asyncio
class TestUserSession:
    async def test_non_existent_user_session(self, client, generate_user_id):
        client.user_id = generate_user_id
        response, content = await self.send_message(client)
        assert response.command == GetGroups.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == Session.NO_SESSION.value, "Response mismatch"

    async def test_existent_user_session(self, create_user_session):
        client = create_user_session
        response, content = await self.send_message(client)
        assert response.command == GetGroups.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == GetGroups.RESPONSE_CHAT_NOT_FOUND.value, "Response mismatch"

    async def test_token_missmatch(self, create_user_session):
        client = create_user_session
        client.token = None
        response, content = await self.send_message(client)
        assert response.command == GetGroups.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == Session.TOKEN_MISSMATCH.value, "Response mismatch"

    async def send_message(self, client) -> tuple:
        data = {}
        response: Message = await client.get_all_groups(data)
        content = response.encode_content_from_json()
        return response, content
