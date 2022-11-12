from global_enums import SendMessageToChat, Protocol
from server.config import server
from server.server_utils.db_utils import async_session
from server.models import Chat, ChatMember
from utils.logger import logger
from utils.protocol import Message, Connection
from sqlalchemy.future import select


@server.message_handler(SendMessageToChat.COMMAND.value)
async def send_message_to_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_id, user_id = content.get("chat_id"), content.get("user_id")
    logger.info(
        f"Attempt send_message_to_chat from user_id {user_id}, to chat_id {chat_id}"
    )
    async with async_session() as session:
        chat_members_id = await session.scalars(
            select(ChatMember.user_id).where(ChatMember.chat_id == chat_id)
        )
        users_id = chat_members_id.all()
        if len(users_id) != 0:
            if user_id in users_id:
                users_id.remove(user_id)
                message_to_chat = Message(
                    SendMessageToChat.COMMAND.value,
                    Protocol.SERVER.value,
                    Protocol.CLIENT.value,
                    Protocol.EMPTY_TOKEN.value,
                    message.content
                )
                for user in users_id:
                    if user in server.sessions:
                        await server.sessions[user]["user_connection"].send_message(
                            message_to_chat
                        )
                response_content = {"response": SendMessageToChat.RESPONSE_MESSAGE_SENT.value}
            else:
                response_content = {"response": SendMessageToChat.RESPONSE_NOT_IN_CHAT.value}
        else:
            response_content = {"response": SendMessageToChat.RESPONSE_CHAT_NOT_FOUND.value}
        response = Message(
            SendMessageToChat.COMMAND.value,
            Protocol.SERVER.value,
            Protocol.CLIENT.value,
            Protocol.EMPTY_TOKEN.value,
            Message.decode_content_to_json(response_content),
        )
        return await connection.send_message(response)
