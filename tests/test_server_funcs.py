import asyncio
import pytest
from global_enums.enum_for_tests import SignIn, SignUP, Token
from utils.protocol import Message, Connection


@pytest.mark.asyncio
async def test_server_command_handler_mapper(test_server, count_routes):
    await asyncio.sleep(2)
    assert len(test_server.command_handler_map) == count_routes


@pytest.mark.asyncio
@pytest.mark.parametrize("data, expected", [(SignIn.GET_EXISTING_USER.value, SignIn.RESPONSE_CONTENT_EXISTING_USER.value),
                                            (SignIn.GET_NON_EXISTING_USER.value, SignIn.RESPONSE_CONTENT_NON_EXISTING_USER.value),
                                            (SignIn.GET_EXISTING_USER_WRONG_PW.value, SignIn.RESPONSE_CONTENT_EXISTING_USER_WRONG_PW.value)])
async def test_sign_in(test_client, data: str, expected):
    await asyncio.sleep(1)
    response = await test_client.write_message_and_wait_answer(test_client.reader, test_client.writer, data.encode(Connection.DATA_CODING_FORMAT))
    message: Message = Message.parse_protocol_message(response)
    content = message.encode_content_from_json()
    assert message.command == "sign_in"
    assert message.sender == "server"
    assert message.receiver == "client"
    #assert len(message.token) == 128
    assert content.get("response") == expected


@pytest.mark.asyncio
@pytest.mark.parametrize("data, expected", [(SignUP.SIGNUP_EXISTING_USER.value, SignUP.RESPONSE_CONTENT_USER_EXISTS.value),
                                            (SignUP.SIGNUP_INCORRECT_LOGIN.value, SignUP.RESPONSE_CONTENT_INCORRECT_LOGIN.value),
                                            (SignUP.SIGNUP_INCORRECT_PW.value, SignUP.RESPONSE_CONTENT_INCORRECT_PW.value),
                                            (SignUP.SIGNUP_NON_EXISTING_USER.value, SignUP.RESPONSE_CONTENT_SUCCESSFUL_SIGNUP.value),])
async def test_sign_up(test_client, data, expected):
    await asyncio.sleep(1)
    response = await test_client.write_message_and_wait_answer(test_client.reader, test_client.writer,
                                                               data.encode(Connection.DATA_CODING_FORMAT))
    message: Message = Message.parse_protocol_message(response)
    content = message.encode_content_from_json()
    assert message.command == "sign_up"
    assert message.sender == "server"
    assert message.receiver == "client"
    assert len(message.token) == 1
    assert content.get("response") == expected
