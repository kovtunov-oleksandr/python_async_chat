import asyncio
import pytest
import pytest_asyncio
from client.client import ChatClient
from server.server_utils.db_utils import async_session
from server.models import User
from tests.utils.generate_logins import (
    generate_single_valid_login,
    generate_single_valid_pw,
    generate_invalid_login_list,
    generate_invalid_password_list,
)

invalid_logins: list = generate_invalid_login_list()
invalid_passwords: list = generate_invalid_password_list()


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture
def generate_valid_login():
    return generate_single_valid_login()


@pytest.fixture
def generate_valid_pw():
    return generate_single_valid_pw()


@pytest.fixture(params=invalid_logins)
def get_invalid_login(request):
    return request.param


@pytest.fixture(params=invalid_passwords)
def get_invalid_password(request):
    return request.param


@pytest_asyncio.fixture(scope="module")
async def client():
    test_client = ChatClient("localhost", 5050)
    asyncio.create_task(test_client.quick_start())
    await asyncio.sleep(1)
    yield test_client
    await test_client.disconnect()


@pytest_asyncio.fixture
async def session():
    async with async_session() as session, session.begin():
        yield session


@pytest.fixture()
def get_amount():
    return 1


@pytest_asyncio.fixture
async def generate_user_in_db(get_amount):
    users = [
        User(nickname=generate_single_valid_login(), password=generate_single_valid_pw()) for i in range(get_amount)
    ]
    async with async_session() as user_session, user_session.begin():
        user_session.add_all(users)
    yield users
    async with async_session() as user_session, user_session.begin():
        [await user_session.delete(user) for user in users]


@pytest_asyncio.fixture
async def create_user_session(client, get_single_generated_user):
    login, password = get_single_generated_user
    data = {"nickname": login, "password": password}
    response = await client.sign_in(data)
    content = response.encode_content_from_json()
    client.token = response.token
    client.user_id = content.get("user_id")
    return client


@pytest_asyncio.fixture
def get_single_generated_user(generate_user_in_db):
    user = generate_user_in_db[0]
    return user.nickname, user.password
