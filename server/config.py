from sqlalchemy.ext.asyncio import create_async_engine
from utils.protocol.server import Server


DATABASE_URL = "sqlite+aiosqlite:///database.db"
engine = create_async_engine(DATABASE_URL, echo=False)


HOST = 'localhost'
PORT = 5050
server = Server(HOST, PORT)
