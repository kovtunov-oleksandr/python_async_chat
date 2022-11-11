from sqlalchemy.future import select
from server.models import Chat, ChatMember, User
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection


@server.message_handler("get_group_members")
async def get_group_members(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_id = content.get("chat_id")
    logger.info(f"Attempt to get chat members from chat id={chat_id} ")
    async with async_session() as session, session.begin():
        chat = await session.scalar(select(Chat).where(Chat.id == chat_id))
        if chat is None:
            response = Message(
                "get_group_members",
                "server",
                "client",
                "_",
                Message.decode_content_to_json({"response": f"THERE IS NO CHAT WITH ID {chat_id}"}),
            )
        else:
            chat_members = await session.scalars(select(ChatMember).where(ChatMember.chat_id == chat_id))
            users_id = [chat_member.user_id for chat_member in chat_members]
            users = await session.scalars(select(User).where(User.id.in_(users_id)))
            users_in_chat = [{"nickname": user.nickname, "id": user.id} for user in users]
            response = Message(
                "get_group_members",
                "server",
                "client",
                "_",
                Message.decode_content_to_json({"response": "LIST OF MEMBERS RECEIVED", "users": users_in_chat}),
            )
        return await connection.send_message(response)
