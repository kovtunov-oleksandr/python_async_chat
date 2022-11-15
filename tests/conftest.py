import asyncio
import pytest
import pytest_asyncio
from tests.utils import generate_invalid_password_list, generate_invalid_login_list

invalid_logins: list = generate_invalid_login_list()
invalid_passwords: list = generate_invalid_password_list()


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture
def generate_valid_login():
    import secrets
    import string

    legacy_chars = string.ascii_letters
    login = "".join(secrets.choice(legacy_chars) for i in range(10))
    return login


@pytest.fixture
def generate_valid_pw():
    import secrets
    import string

    legacy_chars = string.ascii_letters
    password = "".join(secrets.choice(legacy_chars) for i in range(20))
    return password


@pytest.fixture(params=invalid_logins)
def get_invalid_login(request):
    return request.param


@pytest.fixture(params=invalid_passwords)
def get_invalid_password(request):
    return request.param


@pytest_asyncio.fixture(scope="module")
async def client():
    from client.client import ChatClient

    test_client = ChatClient("localhost", 5050)
    asyncio.create_task(test_client.quick_start())
    await asyncio.sleep(1)
    yield test_client
    await test_client.disconnect()


@pytest_asyncio.fixture
async def session():
    from server.server_utils.db_utils import async_session

    async with async_session() as session, session.begin():
        yield session


@pytest_asyncio.fixture
async def generate_user_in_db(generate_valid_login, generate_valid_pw):
    from server.models import User
    from server.server_utils.db_utils import async_session

    login, password = generate_valid_login, generate_valid_pw
    user = User(nickname=login, password=password)
    async with async_session() as user_session, user_session.begin():
        user_session.add(user)
    yield login, password
    async with async_session() as user_session, user_session.begin():
        await user_session.delete(user)


@pytest_asyncio.fixture
async def create_user_session(client, generate_user_in_db):
    login, password = generate_user_in_db
    data = {"nickname": login, "password": password}
    response = await client.sign_in(data)
    content = response.encode_content_from_json()
    client.token = response.token
    client.user_id = content.get("user_id")
    return client
