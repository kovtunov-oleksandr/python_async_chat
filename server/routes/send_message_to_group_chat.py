from server.config import server
from server.server_utils.db_utils import async_session
from server.models import Chat, ChatMember, User
from utils.logger import logger
from utils.protocol import Message, Connection
from sqlalchemy.future import select


@server.message_handler("send_message_to_group_chat")
async def send_message_to_group_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    logger.info(
        f"Send_message_to_group_chat attempt {content.get('chat_name')}, chat_id {content.get('chat_id')}"
    )
    async with async_session() as session:
        sender_id = await session.scalar(
            select(User.id).where(User.nickname == message.sender)
        )
        if "chat_id" not in content:
            chat_id = await session.scalar(
                select(Chat.id).where(Chat.chat_name == content["chat_name"])
            )
        else:
            chat_id = content["chat_id"]
        chat_type = await session.scalar(select(Chat.type).where(Chat.id == chat_id))
        if chat_type == 1:
            result = await session.scalars(
                select(ChatMember.user_id).where(ChatMember.chat_id == chat_id)
            )
            users_id = result.all()
            message_to_chat = Message(
                message.command,
                message.sender,
                content["chat_name"],
                "_",
                content["text"],
            )
            for user_id in users_id:
                if user_id != sender_id:
                    await server.sessions[user_id]["user_connection"].send_message(
                        message_to_chat
                    )
            print(server.sessions)
            response = Message(
                "Send_message_to_group_chat", "server", "_", "_", "{'response': 'ok'}"
            )
            return await connection.send_message(response)
        else:
            response = Message(
                "Send_message_to_group_chat",
                "server",
                "_",
                "_",
                "{'response': 'WRONG CHAT TYPE'}",
            )
            return await connection.send_message(response)
