from sqlalchemy.future import select
from server.models.chat import Chat
from server.models.chatmember import ChatMember
from server.models.user import User
from server.server_utils.db_utils import async_session
from utils.logger import logger
from server.config import server
from utils.protocol.message import Message
from utils.protocol.connection import Connection

@server.message_handler("create_chat")
async def create_chat(message: Message, connection: Connection):
    print("create_chat METHOD")
    content = message.encode_content_from_json()
    logger.info(f"Attempt to create chat {content.get('chat_name')}")
    async with async_session() as session:
        user = await session.scalar(select(Chat).where(Chat.chat_name == content["chat_name"]))
    if user is not None:
        response = Message("create_chat", "server", message.sender, "_", '{"response": "DB has the same chat name"}')
        return await connection.send_message(response)
    else:
        async with async_session() as session, session.begin():
            user = await session.scalar(select(User).where(User.nickname == content["nickname"]))
            chat = Chat(
                chat_name=content["chat_name"],
                creator_id=user.id,
                type=content["chat_type"]
            )
            session.add(chat)
            chat = await session.scalar(select(Chat).where(Chat.chat_name == content["chat_name"]))
            chat_member = ChatMember(
                user_id=user.id,
                chat_id=chat.id,
                permissions=1
            )
            session.add(chat_member)
        response = Message("create_chat", "server", message.sender, "_", '{"response": "chat was created"}')
        return await connection.send_message(response)