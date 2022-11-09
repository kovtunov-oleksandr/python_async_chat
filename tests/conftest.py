import asyncio
import os
import pytest
import pytest_asyncio
from Asyncio_server_client.simple_client import TestClient, TestClient2
from server.main import *

# TODO: create imports to work with test db
# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import sessionmaker
# from server.models.user import Base
# from utils.protocol.server import Server
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "test_database.db")
#
# DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture
def count_routes() -> int:
    dir_path = r'C:/Users/k3nz0/PycharmProjects/python_async_chat/server/routes'
    count = -1
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count


# #  TODO: create test DB
# @pytest_asyncio.fixture(scope="module")
# async def recreate_db(event_loop):
#     engine = create_async_engine(DATABASE_URL, echo=False)
#     async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield async_session
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)


# @pytest_asyncio.fixture(scope="module")
# async def test_server(recreate_db):
#     server = Server()
#     from server.routes.sign_in import sign_in
#     asyncio.create_task(server.run_server())
#     yield server


@pytest_asyncio.fixture(scope="module")
async def test_server(event_loop):
    asyncio.create_task(server.run_server())
    return server


@pytest_asyncio.fixture(scope="module")
async def test_client(test_server):
    client = TestClient2()
    asyncio.create_task(client.start_client())
    return client

