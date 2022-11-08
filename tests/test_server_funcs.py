import pytest
from unittest.mock import patch, Mock

from server.routes.sign_in import sign_in
from utils.protocol import Message, Connection


@pytest.mark.asyncio
async def test_sign_in_handler(server, client):
    await server.run_server()
    # await client.quick_start()
    # data = {"nickname": "admin", "password": "admin"}
    # message = Message("sign_up", "client", "server", "_", Message.decode_content_to_json(data))
    # await client.sigh_in(message)
