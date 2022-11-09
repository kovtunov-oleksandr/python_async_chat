import asyncio
import pytest
from global_enums.enum_for_tests import SignIn, SignUP, Token
from utils.protocol import Message, Connection


@pytest.mark.asyncio
async def test_server_command_handler_mapper(test_server, count_routes):
    await asyncio.sleep(2)
    assert len(test_server.command_handler_map) == count_routes


@pytest.mark.asyncio
@pytest.mark.parametrize("data, expected_token, expected_response", [(SignIn.GET_EXISTING_USER.value, Token.VALID_TOKEN_LENGTH.value, SignIn.RESPONSE_CONTENT_EXISTING_USER.value),
                                            (SignIn.GET_NON_EXISTING_USER.value, Token.EMPTY_TOKEN_LENGTH.value, SignIn.RESPONSE_CONTENT_NON_EXISTING_USER.value),
                                            (SignIn.GET_EXISTING_USER_WRONG_PW.value, Token.EMPTY_TOKEN_LENGTH.value, SignIn.RESPONSE_CONTENT_EXISTING_USER_WRONG_PW.value)])
async def test_sign_in(test_client, expected_token: int, data: str, expected_response: str):
    await asyncio.sleep(1)
    response = await test_client.write_message_and_wait_answer(test_client.reader, test_client.writer, data.encode(Connection.DATA_CODING_FORMAT))
    message: Message = Message.parse_protocol_message(response)
    content = message.encode_content_from_json()
    assert message.command == "sign_in"
    assert message.sender == "server"
    assert message.receiver == "client"
    assert len(message.token) == expected_token
    assert content.get("response") == expected_response



@pytest.mark.asyncio
@pytest.mark.parametrize("data, expected_token, expected_response", [(SignUP.SIGNUP_EXISTING_USER.value,Token.EMPTY_TOKEN_LENGTH.value, SignUP.RESPONSE_CONTENT_USER_EXISTS.value),
                                            (SignUP.SIGNUP_INCORRECT_LOGIN.value, Token.EMPTY_TOKEN_LENGTH.value, SignUP.RESPONSE_CONTENT_INCORRECT_LOGIN.value),
                                            (SignUP.SIGNUP_INCORRECT_PW.value, Token.EMPTY_TOKEN_LENGTH.value, SignUP.RESPONSE_CONTENT_INCORRECT_PW.value),
                                            (SignUP.SIGNUP_NON_EXISTING_USER.value, Token.EMPTY_TOKEN_LENGTH.value, SignUP.RESPONSE_CONTENT_SUCCESSFUL_SIGNUP.value),])
async def test_sign_up(test_client, data: str, expected_token: int, expected_response: str):
    await asyncio.sleep(1)
    response = await test_client.write_message_and_wait_answer(test_client.reader, test_client.writer,
                                                               data.encode(Connection.DATA_CODING_FORMAT))
    message: Message = Message.parse_protocol_message(response)
    content = message.encode_content_from_json()
    assert message.command == "sign_up"
    assert message.sender == "server"
    assert message.receiver == "client"
    assert len(message.token) == expected_token
    assert content.get("response") == expected_response
