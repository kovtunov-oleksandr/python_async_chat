from sqlalchemy.future import select
from server.models import Chat, ChatMember, User
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection
from global_enums import Protocol, CreateChat


@server.message_handler(CreateChat.COMMAND.value)
async def create_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_name, creator_id, second_user_id, chat_type = map(
        lambda x: content.get(x),
        ("chat_name", "user_id", "second_user_id", "chat_type"),
    )
    logger.info(f"Attempt to create chat {chat_name}")
    async with async_session() as session, session.begin():
        chat = await session.scalar(select(Chat).where(Chat.chat_name == chat_name))
        if chat is not None:
            response_content = {"response": CreateChat.RESPONSE_CHAT_NAME_EXISTS.value}
            return await send_message(connection, response_content)
        if chat_type == CreateChat.PRIVATE.value:
            second_user = await session.scalar(select(User).where(User.id == second_user_id))
            if second_user is None:
                response_content = {"response": CreateChat.RESPONSE_SECOND_USER_NOT_FOUND.value}
                return await send_message(connection, response_content)
            chat_id, response_content = await add_chat_and_creator_to_db(session, creator_id, chat_name, chat_type)
            second_chat_member = ChatMember(
                user_id=second_user_id,
                chat_id=chat_id,
                permissions=CreateChat.ADMIN.value,
            )
            session.add(second_chat_member)
            return await send_message(connection, response_content)
        chat_id, response_content = await add_chat_and_creator_to_db(session, creator_id, chat_name, chat_type)
        return await send_message(connection, response_content)


async def send_message(connection: Connection, response: dict):
    response = Message(
        CreateChat.COMMAND.value,
        Protocol.SERVER.value,
        Protocol.CLIENT.value,
        Protocol.EMPTY_TOKEN.value,
        Message.decode_content_to_json(response)
    )
    return await connection.send_message(response)


async def add_chat_and_creator_to_db(session, creator_id, chat_name, chat_type):
    chat = Chat(chat_name=chat_name, creator_id=creator_id, type=chat_type)
    session.add(chat)
    await session.flush()
    creator_chat_member = ChatMember(
        user_id=creator_id,
        chat_id=chat.id,
        permissions=CreateChat.ADMIN.value,
    )
    session.add(creator_chat_member)
    response_content = {
        "response": CreateChat.RESPONSE_CHAT_CREATED.value,
        "chat_id": chat.id,
        "chat_name": chat_name,
    }
    return chat.id, response_content
