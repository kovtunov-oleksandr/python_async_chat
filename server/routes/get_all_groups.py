from sqlalchemy.future import select
from server.models import Chat
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection
from global_enums import Protocol, GetGroups


@server.message_handler(GetGroups.COMMAND.value)
async def get_group_members(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    user_id = content.get("user_id")
    logger.info(f"Attempt getting all groups by user_id: {user_id}")
    async with async_session() as session:
        chats = await session.scalars(select(Chat).where(Chat.type == 1))
        chats = [{"chat_name": chat.chat_name, "chat_id": chat.id} for chat in chats]
        if not chats:
            response = Message(
                GetGroups.COMMAND.value,
                Protocol.SERVER.value,
                Protocol.CLIENT.value,
                Protocol.EMPTY_TOKEN.value,
                Message.decode_content_to_json({"response": GetGroups.RESPONSE_CHAT_NOT_FOUND.value}),
            )
        else:
            response = Message(
                GetGroups.COMMAND.value,
                Protocol.SERVER.value,
                Protocol.CLIENT.value,
                Protocol.EMPTY_TOKEN.value,
                Message.decode_content_to_json({"response": GetGroups.RESPONSE_LIST_RETRIEVED.value, "chats": chats}),
            )
    return await connection.send_message(response)
