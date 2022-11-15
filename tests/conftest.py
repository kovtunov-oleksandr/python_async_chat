import asyncio
import pytest
import pytest_asyncio


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


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

    async with async_session as user_session, user_session.begin():
        yield user_session


@pytest_asyncio.fixture
async def generate_user_in_db():
    import string
    import secrets
    from server.models import User
    from server.server_utils.db_utils import async_session

    nickname = "".join(secrets.choice(string.ascii_letters) for i in range(10))
    password = "".join(secrets.choice(string.printable.replace(" ", "")) for i in range(10))
    user = User(nickname=nickname, password=password)
    async with async_session as user_session, user_session.begin():
        user_session.add(user)
    yield user.id, nickname, password
    async with async_session as user_session, user_session.begin():
        user_session.delete(user)


@pytest_asyncio.fixture
async def sign_in(client, generate_user_in_db):
    user_id, nickname, password = generate_user_in_db
    data = {"nickname": nickname, "password": password}
    response = await client.sign_in(data)
    client.token = response.token
    client.user_id = user_id
    return client


@pytest.fixture
def generate_chat_name():
    import string
    import secrets

    chat_name = "".join(secrets.choice(string.ascii_letters) for i in range(10))
    return chat_name


@pytest_asyncio.fixture
async def generate_chat_in_db(generate_user_in_db, generate_chat_name):
    from server.models import Chat
    from server.server_utils.db_utils import async_session

    chat_name = generate_chat_name
    creator_id, _, _ = generate_user_in_db
    chat = Chat(chat_name=chat_name, creator_id=creator_id, type=1)
    async with async_session as user_session, user_session.begin():
        user_session.add(chat)
    yield chat.chat_name
    async with async_session as user_session, user_session.begin():
        user_session.add(chat)
