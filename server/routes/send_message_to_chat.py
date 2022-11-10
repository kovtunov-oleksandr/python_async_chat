from server.config import server
from server.server_utils.db_utils import async_session
from server.models import Chat, ChatMember, User
from utils.logger import logger
from utils.protocol import Message, Connection
from sqlalchemy.future import select


@server.message_handler("send_message_to_chat")
async def send_message_to_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    logger.info(
        f"Attempt send_message_to_chat from user_id {content.get('user_id')}, to chat_id {content.get('chat_id')}"
    )
    async with async_session() as session:
        result = await session.scalars(
            select(ChatMember.user_id).where(
                ChatMember.chat_id == content.get("chat_id")
            )
        )
        users_ids = result.all()
        message_to_chat = Message(
            message.command, "server", "client", "_", message.content
        )
        for user_id in users_ids:
            if user_id != content.get("user_id"):
                await server.sessions[user_id]["user_connection"].send_message(
                    message_to_chat
                )
        response = Message(
            "Send_message_to_chat", "server", "client", "_", "{'response': 'OK'}"
        )
        return await connection.send_message(response)
