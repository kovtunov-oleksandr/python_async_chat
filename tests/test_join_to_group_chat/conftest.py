import random
import pytest
import pytest_asyncio
from server.server_utils.db_utils import async_session
from server.models import ChatMember
from global_enums import CreateChat


@pytest.fixture
def get_amount():
    return 2


@pytest.fixture
def generate_non_exist_chat_id():
    num = random.randint(9999, 99999)
    return num


@pytest_asyncio.fixture
async def generate_chat_member(generate_user_in_db, get_single_chat):
    user = generate_user_in_db[0]
    chat = get_single_chat
    async with async_session() as user_session, user_session.begin():
        chat_member = ChatMember(user_id=user.id, chat_id=chat.id, permissions=CreateChat.USER.value)
        user_session.add(chat_member)
    yield chat_member
    async with async_session() as user_session, user_session.begin():
        await user_session.delete(chat)
