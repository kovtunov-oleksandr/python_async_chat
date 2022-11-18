import pytest
import pytest_asyncio
from sqlalchemy import delete

from server.models import User


@pytest.fixture
def get_amount():
    return 1


@pytest_asyncio.fixture
async def get_user(generate_valid_login, generate_valid_pw, session):
    yield generate_valid_login, generate_valid_pw
    query = delete(User).where(User.nickname == generate_valid_login)
    await session.execute(query)
