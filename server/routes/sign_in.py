import jwt
from sqlalchemy.future import select
from server.config import server, token_key, algorithm
from server.models.session import UserSession
from server.models.user import User
from server.server_utils.db_utils import async_session
from utils.logger import logger
from utils.protocol.message import Message
from utils.protocol.connection import Connection


@server.message_handler("sign_in")
async def sign_in(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    logger.info(f"Sign in attempt {content.get('nickname')}, {content.get('password')}")
    async with async_session() as session:
        result = await session.scalars(select(User).where(User.nickname == content["nickname"]))
        user = result.first()
    if user is not None and user.password == content.get('password'):
        token = await create_session(user, content, connection)
        response = Message("sign_in", "server", message.sender,token, '{"response": "LOG IN SUCCESSFUL"}')
        return await connection.send_message(response)
    elif user is not None and user.password != content.get('password'):
        response = Message("sign_in", "server", message.sender, "_", '{"response": "INCORRECT PASSWORD"}')
        return await connection.send_message(response)
    response = Message("sign_in", "server", message.sender, "_", '{"response": "USER NOT FOUND"}')
    return await connection.send_message(response)


async def create_session(user: User, content: dict, connection: Connection):
    token = jwt.encode(content, token_key, algorithm)
    session = UserSession(user.id, user.nickname, token)
    server.sessions[user.id] = session
    return token
