from sqlalchemy.future import select
from server.models import Chat
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection


@server.message_handler("get_all_groups")
async def get_group_members(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    user_id = content.get("user_id")
    logger.info(f"Attempt getting all groups by user_id: {user_id}")
    async with async_session() as session:
        chats = await session.scalars(select(Chat).where(Chat.type == 1))
        chats_is_none = await session.scalars(select(Chat).where(Chat.type == 1))
        if chats_is_none.first() is None:
            response = Message(
                "get_all_groups",
                "server",
                "client",
                "_",
                Message.decode_content_to_json({"response": f"THERE IS NO CHAT"}),
            )
        else:
            chats = [{"chat_name": chat.chat_name, "chat_id": chat.id} for chat in chats]
            response = Message(
                "get_all_groups",
                "server",
                "client",
                "_",
                Message.decode_content_to_json({"response": "LIST OF CHATS RECEIVED", "chats": chats}),
            )
        return await connection.send_message(response)
