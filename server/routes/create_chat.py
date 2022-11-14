import asyncio

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
        else:
            if chat_type == 0:
                response_content = await asyncio.create_task(
                    second_user_verification(second_user_id, session)
                )
            if chat_type == 1 or response_content is True:
                chat = Chat(chat_name=chat_name, creator_id=creator_id, type=chat_type)
                session.add(chat)
                await session.flush()
                creator_chat_member = ChatMember(
                    user_id=creator_id,
                    chat_id=chat.id,
                    permissions=CreateChat.ADMIN.value,
                )
                session.add(creator_chat_member)
                if chat_type == 0:
                    second_chat_member = ChatMember(
                        user_id=second_user_id,
                        chat_id=chat.id,
                        permissions=CreateChat.ADMIN.value,
                    )
                    session.add(second_chat_member)
                response_content = {
                        "response": CreateChat.RESPONSE_CHAT_CREATED.value,
                        "chat_id": chat.id,
                        "chat_name": chat_name,
                }
    response = Message(
        CreateChat.COMMAND.value,
        Protocol.SERVER.value,
        Protocol.CLIENT.value,
        Protocol.EMPTY_TOKEN.value,
        Message.decode_content_to_json(response_content)
    )
    return await connection.send_message(response)


async def second_user_verification(second_user_id: int, session: async_session):
    if second_user_id is None:
        response_content = {"response": CreateChat.RESPONSE_SECOND_USER_SPECIFIED.value}
    else:
        second_user = await session.scalar(
            select(User).where(User.id == second_user_id)
        )
        if second_user is not None:
            response_content = True
        else:
            response_content = {"response": CreateChat.RESPONSE_SECOND_USER_NOT_FOUND.value}
    return response_content
