import pytest

from client.client import ChatClient
from server.config import server


@pytest.fixture(scope="module")
def server():
    return server


@pytest.fixture(scope="module")
def client():
    client = ChatClient("localhost", 5050)
    return client


