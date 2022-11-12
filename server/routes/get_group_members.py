from sqlalchemy.future import select
from server.models import Chat, ChatMember, User
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection
from global_enums import Protocol, GetMembers


@server.message_handler(GetMembers.COMMAND.value)
async def get_group_members(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_id = content.get("chat_id")
    logger.info(f"Attempt to get chat members from chat id={chat_id} ")
    async with async_session() as session, session.begin():
        chat = await session.scalar(select(Chat).where(Chat.id == chat_id))
        if chat is None:
            response = Message(
                GetMembers.COMMAND.value,
                Protocol.SERVER.value,
                Protocol.CLIENT.value,
                Protocol.EMPTY_TOKEN.value,
                Message.decode_content_to_json({"response": f"{GetMembers.RESPONSE_CHAT_NOT_FOUND.value} {chat_id}"}),
            )
        else:
            chat_members = await session.scalars(select(ChatMember).where(ChatMember.chat_id == chat_id))
            users_id = [chat_member.user_id for chat_member in chat_members]
            users = await session.scalars(select(User).where(User.id.in_(users_id)))
            users_in_chat = [{"nickname": user.nickname, "id": user.id} for user in users]
            response = Message(
                GetMembers.COMMAND.value,
                Protocol.SERVER.value,
                Protocol.CLIENT.value,
                Protocol.EMPTY_TOKEN.value,
                Message.decode_content_to_json(
                    {"response": GetMembers.RESPONSE_LIST_RETRIEVED.value, "users": users_in_chat}
                ),
            )
        return await connection.send_message(response)
