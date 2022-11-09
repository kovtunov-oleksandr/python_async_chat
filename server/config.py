from sqlalchemy.ext.asyncio import create_async_engine
from utils.protocol.server import Server
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"
engine = create_async_engine(DATABASE_URL, echo=False)

HOST = "localhost"
PORT = 5050
server = Server(HOST, PORT)
