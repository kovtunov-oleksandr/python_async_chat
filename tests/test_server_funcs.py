import asyncio
import pytest
from global_enums.enum_for_tests import SignIn, SignUP, Token, Chat, Commands, Misc
from utils.protocol import Message


# @pytest.mark.asyncio
# async def test_server_command_handler_mapper(test_server, count_routes):
#     await asyncio.sleep(2)
#     assert len(test_server.command_handler_map) == count_routes


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "login, password, expected_token, expected_response",
    [
        (SignUP.INCORRECT_LOGIN.value, SignUP.CORRECT_PW.value, Token.EMPTY_TOKEN_LENGTH.value, SignUP.RESPONSE_CONTENT_INCORRECT_LOGIN.value),
        (SignUP.NEW_USER.value, SignUP.INCORRECT_PW.value, Token.EMPTY_TOKEN_LENGTH.value, SignUP.RESPONSE_CONTENT_INCORRECT_PW.value),
        (SignUP.NEW_USER.value, SignUP.CORRECT_PW.value, Token.EMPTY_TOKEN_LENGTH.value, SignUP.RESPONSE_CONTENT_SUCCESSFUL_SIGNUP.value),
        (SignUP.NEW_USER.value, SignUP.CORRECT_PW.value, Token.EMPTY_TOKEN_LENGTH.value, SignUP.RESPONSE_CONTENT_USER_EXISTS.value),


    ]
)
async def test_sign_up(test_client, login, password, expected_token: int, expected_response: str):
    data = {"nickname": login, "password": password}
    command, sender, receiver, token = "sign_up", "client", "server", "_"
    message = Message(command, sender, receiver, token, Message.decode_content_to_json(data))
    response = await test_client.send_message(message)
    message: Message = Message.parse_protocol_message(response)
    content = message.encode_content_from_json()
    assert message.command == command
    assert message.sender == receiver
    assert message.receiver == sender
    assert len(message.token) == expected_token
    assert content.get("response") == expected_response


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "login, password, expected_token, expected_response",
    [
        (SignIn.NOT_EXISTING_USER.value, SignIn.EXISTING_PW.value, Token.EMPTY_TOKEN_LENGTH.value, SignIn.RESPONSE_USER_NOT_FOUND.value),
        (SignIn.EXISTING_USER.value, SignIn.WRONG_PW.value, Token.EMPTY_TOKEN_LENGTH.value, SignIn.RESPONSE_INCORRECT_PW.value),
        (SignIn.EXISTING_USER.value, SignIn.EXISTING_PW.value, Token.VALID_TOKEN_LENGTH.value, SignIn.RESPONSE_SUCCESSFULL_LOGIN.value)
    ]
)
async def test_sign_in(test_client, login, password, expected_token: int, expected_response: str):
    data = {"nickname": login, "password": password}
    command, sender, receiver, token = "sign_in", "client", "server", "_"
    message = Message(command, sender, receiver, token, Message.decode_content_to_json(data))
    response = await test_client.send_message(message)
    message: Message = Message.parse_protocol_message(response)
    content = message.encode_content_from_json()
    assert message.command == command
    assert message.sender == receiver
    assert message.receiver == sender
    assert len(message.token) == expected_token
    assert content.get("response") == expected_response


@pytest.mark.asyncio
async def test_user_session(test_client):
    data = {"nickname": test_client.nickname, "user_id": "_"}
    command, sender, receiver, token = "no_method", "client", "server", "_"
    message = Message(command, "client", "server", token, Message.decode_content_to_json(data))
    response = await test_client.send_message(message)
    message: Message = Message.parse_protocol_message(response)
    content = message.encode_content_from_json()
    assert message.command == command
    assert message.sender == receiver
    assert message.receiver == sender
    assert content.get("response") == Token.RESPONSE_NO_USER_IN_SESSION.value


@pytest.mark.asyncio
async def test_user_token_auth_fail(test_client):
    data = {"nickname": test_client.nickname, "user_id": test_client.user_id}
    command, sender, receiver, token = "no_method", "client", "server", "_"
    message = Message(command, sender, receiver, token, Message.decode_content_to_json(data))
    response = await test_client.send_message(message)
    message: Message = Message.parse_protocol_message(response)
    content = message.encode_content_from_json()
    assert message.command == command
    assert message.sender == receiver
    assert message.receiver == sender
    assert content.get("response") == Token.RESPONSE_TOKEN_AUTH_FAIL.value


@pytest.mark.asyncio
@pytest.mark.parametrize("chat_name, expected_response", [
    (Chat.NAME.value, Chat.RESPONSE_CHAT_CREATED.value),
    (Chat.NAME.value, Chat.RESPONSE_CHAT_NAME_EXISTS.value)
])
async def test_create_chat(test_client,chat_name, expected_response):
    data = {"chat_name": chat_name, "user_id": test_client.user_id, "chat_type": Chat.GROUP_CHAT_TYPE.value}
    command, sender, receiver, token = Commands.CREATE_CHAT.value, Misc.CLIENT.value, Misc.SERVER.value, test_client.token
    message = Message(command, sender, receiver, token, Message.decode_content_to_json(data))
    response = await test_client.send_message(message)
    message: Message = Message.parse_protocol_message(response)
    content = message.encode_content_from_json()
    assert message.command == command
    assert message.sender == receiver
    assert message.receiver == sender
    assert content.get("response") == expected_response

# @pytest.mark.asyncio
# async def test_sign_up_2(test_client):
#     data = {"nickname": "admin", "password": "adminadmin"}
#     command, sender, receiver, token = "sign_up", "client", "server", "_"
#     response = await test_client.sign_in(data)
#     message: Message = Message.parse_protocol_message(response)
#     content = message.encode_content_from_json()
#     assert message.command == command
#     assert message.sender == receiver
#     assert message.receiver == sender
#     #assert len(message.token) == expected_token
#     assert content.get("response") == SignIn.RESPONSE_SUCCESSFULL_LOGIN