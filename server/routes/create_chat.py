from sqlalchemy.future import select
from server.models import Chat, ChatMember, User
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection


@server.message_handler("create_chat")
async def create_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_name, user_id, chat_type = map(lambda x: content.get(x), ("chat_name", "user_id", "chat_type"))
    logger.info(f"Attempt to create chat {chat_name}")
    async with async_session() as session, session.begin():
        chat = await session.scalar(select(Chat).where(Chat.chat_name == chat_name))
    if chat is not None:
        response = Message(
            "create_chat", "server", "_", "_", Message.decode_content_to_json('{"response": "Chat name is not unique"}')
        )
    else:
        chat = Chat(chat_name=chat_name, creator_id=user_id, type=chat_type)
        session.add(chat)
        chat = await session.scalar(select(Chat).where(Chat.chat_name == chat_name))
        chat_member = ChatMember(user_id=user_id, chat_id=chat.id, permissions=1)
        session.add(chat_member)
        response = Message(
            "create_chat",
            "server",
            "_",
            "_",
            Message.decode_content_to_json(
                f'{"response": "Сhat was created", "chat_id": {chat.id}, "chat_name":{chat_name}}'
            ),
        )
    return await connection.send_message(response)
