from sqlalchemy.future import select
from global_enums import LeaveChat, Protocol
from server.models import Chat, ChatMember
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection


@server.message_handler(LeaveChat.COMMAND.value)
async def leave_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_id, user_id = content.get("chat_id"), content.get("user_id")
    logger.info(f"Attempt to leave chat {chat_id} by user_id {user_id}")
    async with async_session() as session, session.begin():
        chat_members = await session.scalars(select(ChatMember).where(ChatMember.chat_id == chat_id))
        users_in_chat = chat_members.all()
        if users_in_chat:
            if [await session.delete(user) for user in users_in_chat if user.user_id == user_id]:
                if len(users_in_chat) == 1:
                    await session.delete(await session.scalar(select(Chat).where(Chat.id == chat_id)))
                response_content = {"response": LeaveChat.RESPONSE_LEFT_CHAT.value}
            else:
                response_content = {"response": LeaveChat.RESPONSE_NOT_CHAT_MEMBER.value}
        else:
            response_content = {"response": LeaveChat.RESPONSE_CHAT_NOT_FOUND.value}
    response = Message(
        LeaveChat.COMMAND.value,
        Protocol.SERVER.value,
        Protocol.CLIENT.value,
        Protocol.EMPTY_TOKEN.value,
        Message.decode_content_to_json(response_content),
    )
    return await connection.send_message(response)
