import pytest
from server.models import User
from utils.protocol.message import Message
from global_enums import SignUP, Protocol
from sqlalchemy.future import select


@pytest.mark.asyncio
class TestSignUp:
    async def test_successful_sign_up(self, client, generate_correct_login_and_pw, session):
        login, password = generate_correct_login_and_pw
        data = {"nickname": login, "password": password}
        response: Message = await client.sign_up(data)
        content = response.encode_content_from_json()
        assert response.command == SignUP.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == SignUP.RESPONSE_REGISTRATION_SUCCESS.value
        user = await session.scalar(select(User).where(User.nickname == login))
        assert user is not None

    async def test_fail_sign_up_login_exists(self, client, generate_user_in_db):
        login, password = generate_user_in_db
        data = {"nickname": login, "password": password}
        response: Message = await client.sign_up(data)
        content = response.encode_content_from_json()
        assert response.command == SignUP.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == SignUP.RESPONSE_LOGIN_EXISTS.value

    async def test_sign_up_incorrect_password(self, client, generate_incorrect_password):
        login, password = generate_incorrect_password
        data = {"nickname": login, "password": password}
        response: Message = await client.sign_up(data)
        content = response.encode_content_from_json()
        assert response.command == SignUP.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == SignUP.RESPONSE_INVALID_PASSWORD.value

    async def test_sign_up_incorrect_login(self, client, get_invalid_login, generate_valid_pw):
        login, password = get_invalid_login, generate_valid_pw
        data = {"nickname": login, "password": password}
        response: Message = await client.sign_up(data)
        content = response.encode_content_from_json()
        assert response.command == SignUP.COMMAND.value
        assert response.sender == Protocol.SERVER.value
        assert response.receiver == Protocol.CLIENT.value
        assert content.get("response") == SignUP.RESPONSE_INVALID_NICKNAME.value
