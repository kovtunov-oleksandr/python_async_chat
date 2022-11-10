from server.config import server
from server.server_utils.db_utils import async_session
from server.models import Chat, ChatMember
from utils.logger import logger
from utils.protocol import Message, Connection
from sqlalchemy.future import select


@server.message_handler("send_message_to_chat")
async def send_message_to_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_id, user_id = content.get("chat_id"), content.get("user_id")
    logger.info(
        f"Attempt send_message_to_chat from user_id {user_id}, to chat_id {chat_id}"
    )
    async with async_session() as session:
        chat = await session.scalar(select(Chat).where(Chat.id == chat_id))
        if chat is None:
            response = Message(
                "send_message_to_chat",
                "server",
                "client",
                "_",
                Message.decode_content_to_json(
                    {"response": "THIS CHAT DOES NOT EXIST"}
                ),
            )
            return await connection.send_message(response)
        else:
            member_in_chat = await session.scalar(
                select(ChatMember).where(
                    ChatMember.user_id == user_id, ChatMember.chat_id == chat_id
                )
            )
            if member_in_chat is not None:
                chat_members_id = await session.scalars(
                    select(ChatMember.user_id).where(ChatMember.chat_id == chat_id)
                )
                users_id = chat_members_id.all()
                message_to_chat = Message(
                    message.command, "server", "client", "_", message.content
                )
                for user in users_id:
                    if user != user_id and user in server.sessions:
                        await server.sessions[user]["user_connection"].send_message(
                            message_to_chat
                        )
                response = Message(
                    "Send_message_to_chat",
                    "server",
                    "client",
                    "_",
                    Message.decode_content_to_json({"response": "MESSAGE SENT"}),
                )
                return await connection.send_message(response)
            else:
                response = Message(
                    "send_message_to_chat",
                    "server",
                    "client",
                    "_",
                    Message.decode_content_to_json(
                        {"response": "YOU ARE NOT IN THIS CHAT"}
                    ),
                )
                return await connection.send_message(response)
