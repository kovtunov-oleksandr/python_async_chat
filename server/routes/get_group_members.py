from sqlalchemy.future import select
from server.models import Chat, ChatMember, User
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection


@server.message_handler("get_group_members")
async def get_group_members(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_name = content.get("chat_name")
    logger.info(f"Attempt to get chat members from {chat_name} chat")
    async with async_session() as session, session.begin():
        chat = await session.scalar(select(Chat).where(Chat.chat_name == chat_name))
        if chat is None:
            response = Message(
                "create_chat",
                "server",
                "client",
                "_",
                Message.decode_content_to_json({"response": f"WE DID NOT HAVE CHAT WITH NAME {chat_name}"}),
            )
        else:
            chat_members = await session.scalars(select(ChatMember).where(ChatMember.chat_id == chat.id))
            users_id = [chat_member.user_id for chat_member in chat_members]
            users = await session.scalars(select(User).where(User.id.in_(users_id)))
            users_in_chat = [{"nickname": user.nickname, "id": user.id} for user in users]
            response = Message(
                "create_chat",
                "server",
                "client",
                "_",
                Message.decode_content_to_json({"response": "LIST OF MEMBERS RECEIVED", "users": users_in_chat}),
            )
        return await connection.send_message(response)
