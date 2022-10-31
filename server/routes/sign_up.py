from server.config import server
from server.models.user import User
from server.server_utils.db_utils import async_session
from utils.protocol.message import Message
from utils.protocol.connection import Connection
from utils.logger import logger
from sqlalchemy.future import select
import json


@server.message_handler("sign_up")
async def sign_up(request: Message, connection: Connection):
    content = json.loads(request.content)
    logger.info(
        f"Sign up attempt {content.get('nickname'), content.get('password'), content.get('email')}"
    )
    credentials = check_nickname_password_credentials(content.get("nickname"), content.get("password"))
    if next(credentials) is not True:
        return await handle_response(
            request.sender,
            "NICKNAME CANNOT START WITH A SPACE AND MUST CONTAINS ONLY 4 TO 16 CHARACTERS OF THE ENGLISH ALPHABET",
            connection,
        )
    if next(credentials) is not True:
        return await handle_response(
            request.sender,
            "PASSWORD CANNOT START WITH A SPACE AND CONTAINS MORE THAN 50 CHARACTERS",
            connection,
        )
    async with async_session() as session:
        is_nickname_in_db = await session.scalar(
            select(User).where(User.nickname == content["nickname"])
        )
        if is_nickname_in_db is not None:
            return await handle_response(
                request.sender, "THIS LOGIN IS NOT UNIQUE", connection
            )
        else:
            return await handle_response(
                request.sender, "REGISTRATION IS SUCCESSFUL", connection, content
            )


def check_nickname_password_credentials(nickname: str, password: str):
    if (
            4 <= len(nickname) <= 16
            and (nickname.isascii() is True and nickname.isalpha() is True)
            and nickname[0] != " "
    ):
        yield True
    else:
        yield False
    if len(password) <= 50 and password.isascii() is True and password[0] != " ":
        yield True
    yield False


async def add_user_to_db(content: dict, connection: Connection):
    user = User(
        nickname=content["nickname"],
        password=content["password"],
        email=content.get("email"),
    )
    async with async_session() as session, session.begin():
        session.add(user)
    logger.info(
        f"New user was registered: <{user.nickname}>, connection: {connection.writer.get_extra_info('peername')}"
    )


async def handle_response(
    sender: str, response_text: str, connection: Connection, content: dict = None
):
    response = Message(
        "sign_up", "server", sender, "_", json.dumps({"response": response_text})
    )
    if response_text == "REGISTRATION IS SUCCESSFUL":
        await add_user_to_db(content, connection)
    return await connection.send_message(response)
