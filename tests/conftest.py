import asyncio
import pytest
import pytest_asyncio
from client.client import ChatClient


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest_asyncio.fixture(scope="module")
async def recreate_db():
    from server.server_utils.db_utils import engine
    from server.models.user import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="module")
async def test_client(recreate_db):
    from simple_client import TestClient
    client = TestClient()
    asyncio.create_task(client.start_client())
    await asyncio.sleep(1)
    return client


# TODO: Real chat client (not working atm)
# @pytest_asyncio.fixture(scope="module")
# async def test_client(recreate_db):
#     client = ChatClient("localhost", 5050)
#     asyncio.create_task(client.quick_start())
#     return client



# @pytest.fixture
# def count_routes() -> int:
#     dir_path = r'C:/Users/k3nz0/PycharmProjects/python_async_chat/server/routes'  # TODO: reformat string path
#     count = 0
#     for path in os.listdir(dir_path):
#         if os.path.isfile(os.path.join(dir_path, path)) and os.path.basename(os.path.join(dir_path, path)) != "__init__.py":
#             count += 1
#     return count





