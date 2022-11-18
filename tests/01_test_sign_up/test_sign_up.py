import pytest
from server.models import User
from utils.protocol.message import Message
from global_enums import SignUP, Protocol
from sqlalchemy.future import select


@pytest.mark.asyncio
class TestSignUp:
    async def test_successful_sign_up(self, client, get_user, session):
        response, content = await self.send_message(client, get_user)
        assert response.command == SignUP.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == SignUP.RESPONSE_REGISTRATION_SUCCESS.value, "Response mismatch"
        user = await session.scalar(select(User).where(User.nickname == get_user[0]))
        assert user is not None, "User not created in DB"

    async def test_sign_up_login_exists(self, client, get_single_generated_user):
        user = get_single_generated_user
        response, content = await self.send_message(client, (user.nickname, user.password))
        assert response.command == SignUP.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == SignUP.RESPONSE_LOGIN_EXISTS.value, "Response mismatch"

    async def test_sign_up_incorrect_password(self, client, generate_valid_login, get_invalid_password):
        response, content = await self.send_message(client, (generate_valid_login, get_invalid_password))
        assert response.command == SignUP.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == SignUP.RESPONSE_INVALID_PASSWORD.value, "Response mismatch"

    async def test_sign_up_incorrect_login(self, client, get_invalid_login, generate_valid_pw):
        response, content = await self.send_message(client, (get_invalid_login, generate_valid_pw))
        assert response.command == SignUP.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == SignUP.RESPONSE_INVALID_NICKNAME.value, "Response mismatch"

    async def send_message(self, client, data: tuple) -> tuple:
        login, password = data[0], data[1]
        data = {"nickname": login, "password": password}
        response: Message = await client.sign_up(data)
        content = response.encode_content_from_json()
        return response, content
