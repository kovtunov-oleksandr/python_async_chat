from sqlalchemy.future import select
from server.config import server
from server.server_utils.db_utils import async_session
from server.models import Chat, ChatMember
from utils.protocol import Message, Connection
from utils.logger import logger
from global_enums import Protocol, JoinGroup


@server.message_handler(JoinGroup.COMMAND.value)
async def join_to_group_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_id, user_id = content.get("chat_id"), content.get("user_id")
    logger.info(f"Attempt to join user (user_id: {user_id}) to chat (chat_id: {chat_id})")
    async with async_session() as session, session.begin():
        chat = await session.scalar(select(Chat).where(Chat.id == chat_id))
        if chat is None:
            response = Message(
                JoinGroup.COMMAND.value,
                Protocol.SERVER.value,
                Protocol.CLIENT.value,
                Protocol.EMPTY_TOKEN.value,
                Message.decode_content_to_json({"response": JoinGroup.RESPONSE_CHAT_NOT_FOUND.value}),
            )
        else:
            member_in_chat = await session.scalar(
                select(ChatMember).where(ChatMember.user_id == user_id, ChatMember.chat_id == chat.id)
            )
            if member_in_chat is not None:
                response = Message(
                    JoinGroup.COMMAND.value,
                    Protocol.SERVER.value,
                    Protocol.CLIENT.value,
                    Protocol.EMPTY_TOKEN.value,
                    Message.decode_content_to_json({"response": JoinGroup.RESPONSE_ALREADY_IN_CHAT.value}),
                )
            else:
                chat_member = ChatMember(user_id=user_id, chat_id=chat_id, permissions=0)
                session.add(chat_member)
                response = Message(
                    JoinGroup.COMMAND.value,
                    Protocol.SERVER.value,
                    Protocol.CLIENT.value,
                    Protocol.EMPTY_TOKEN.value,
                    Message.decode_content_to_json(
                        {
                            "response": JoinGroup.RESPONSE_CHAT_JOINED.value,
                            "chat_id": chat.id,
                            "chat_name": chat.chat_name,
                        }
                    ),
                )
                logger.info(
                    f"User (user_id: {user_id} was added to chat (chat_id: {chat.id}), "
                    + f"connection: {connection.writer.get_extra_info('peername')}"
                )
    return await connection.send_message(response)
