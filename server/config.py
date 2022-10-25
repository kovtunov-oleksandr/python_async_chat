from sqlalchemy.ext.asyncio import create_async_engine
from utils.protocol.server import Server


DATABASE_URL = "sqlite+aiosqlite:///C:/Users/k3nz0/PycharmProjects/python_async_chat/server/server_utils/database.db"
engine = create_async_engine(DATABASE_URL, echo=False)

token_key = "super_secret_key"
algorithm = "HS256"

HOST = "localhost"
PORT = 5050
server = Server(HOST, PORT)
