from sqlalchemy.future import select
from server.config import server
from server.server_utils.db_utils import async_session
from server.models import Chat, ChatMember
from utils.protocol import Message, Connection
from utils.logger import logger


@server.message_handler("join_to_chat")
async def join_to_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_id, user_id, permission = map(
        lambda x: content.get(x), ("chat_id", "user_id", "permission")
    )
    logger.info(f"Attempt to join to chat from {user_id}, {chat_id}")
    async with async_session() as session, session.begin():
        chat = await session.scalar(select(Chat).where(Chat.chat_id == chat_id))
        if chat is None:
            response = Message(
                "join_to_chat",
                "server",
                "client",
                "_",
                Message.decode_content_to_json(
                    {"response": "THIS CHAT DOES NOT EXIST"}
                ),
            )
        else:
            result = await session.scalar(select(ChatMember).where(ChatMember.user_id == user_id))
            if result is not None:
                response = Message(
                    "join_to_chat",
                    "server",
                    "client",
                    "_",
                    Message.decode_content_to_json(
                        {"response": "YOU ARE ALREADY IN THIS CHAT"}
                    ),
                )
            else:
                chat_member = ChatMember(
                    user_id=user_id, chat_id=chat_id, permissions=permission
                )
                session.add(chat_member)
                response = Message(
                    "join_to_chat",
                    "server",
                    "client",
                    "_",
                    Message.decode_content_to_json(
                        {
                            "response": "YOU JOINED THE CHAT",
                            "chat_id": chat.id,
                            "chat_name": chat.name,
                        }
                    ),
                )
                logger.info(
                    f"User was added to chat: <{user_id}> - <{chat_id}>, "
                    + f"connection: {connection.writer.get_extra_info('peername')}"
                )
    return await connection.send_message(response)
