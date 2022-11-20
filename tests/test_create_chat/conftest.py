import random
import pytest
import pytest_asyncio
from tests.utils.generate_chat_name import generate_chat_name
from sqlalchemy import delete
from server.models import Chat

@pytest.fixture
def get_amount():
    return 2

@pytest.fixture
def generate_non_exist_user_id():
    num = random.randint(9999, 99999)
    return num

@pytest_asyncio.fixture
async def get_chat_name(session):
    chat_name = generate_chat_name()
    yield chat_name
    query = delete(Chat).where(Chat.chat_name == chat_name)
    await session.execute(query)

