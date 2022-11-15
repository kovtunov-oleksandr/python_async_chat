import asyncio
from global_enums import SendMessageToChat, Protocol
from server.config import server
from server.server_utils.db_utils import async_session
from server.models import ChatMember, PendingMessages
from utils.logger import logger
from utils.protocol import Message, Connection
from sqlalchemy.future import select


@server.message_handler(SendMessageToChat.COMMAND.value)
async def send_message_to_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_id, user_id = content.get("chat_id"), content.get("user_id")
    logger.info(f"Attempt send_message_to_chat from user_id {user_id}, to chat_id {chat_id}")
    async with async_session() as session, session.begin():
        chat_members_id = await session.scalars(select(ChatMember.user_id).where(ChatMember.chat_id == chat_id))
        users_id = chat_members_id.all()
        if users_id:
            if user_id in users_id:
                users_id.remove(user_id)
                message_to_chat = Message(
                    SendMessageToChat.COMMAND.value,
                    Protocol.SERVER.value,
                    Protocol.CLIENT.value,
                    Protocol.EMPTY_TOKEN.value,
                    message.content,
                )
                tasks = [
                    asyncio.create_task(server.sessions[user]["user_connection"].send_message(message_to_chat))
                    if user in server.sessions
                    else asyncio.create_task(add_message_for_pending(user, chat_id, message_to_chat, session))
                    for user in users_id
                ]
                await asyncio.gather(*tasks)
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


async def add_message_for_pending(user_id: int, chat_id: int, message: Message, session: async_session):
    pending_message = PendingMessages(user_id=user_id, chat_id=chat_id, message=message.form_protocol())
    session.add(pending_message)
