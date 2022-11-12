from sqlalchemy.future import select
from server.models import Chat, ChatMember
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection
from global_enums import Protocol, CreateChat


@server.message_handler(CreateChat.COMMAND.value)
async def create_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_name, user_id, chat_type = map(lambda x: content.get(x), ("chat_name", "user_id", "chat_type"))
    logger.info(f"Attempt to create chat {chat_name}")
    async with async_session() as session, session.begin():
        chat = await session.scalar(select(Chat).where(Chat.chat_name == chat_name))
        if chat is not None:
            response = Message(
                CreateChat.COMMAND.value,
                Protocol.SERVER.value,
                Protocol.CLIENT.value,
                Protocol.EMPTY_TOKEN.value,
                Message.decode_content_to_json({"response": CreateChat.RESPONSE_CHAT_NAME_EXISTS.value}),
            )
        else:
            chat = Chat(chat_name=chat_name, creator_id=user_id, type=chat_type)
            session.add(chat)
            await session.flush()
            chat_member = ChatMember(user_id=user_id, chat_id=chat.id, permissions=CreateChat.ADMIN.value)
            session.add(chat_member)
            response = Message(
                CreateChat.COMMAND.value,
                Protocol.SERVER.value,
                Protocol.CLIENT.value,
                Protocol.EMPTY_TOKEN.value,
                Message.decode_content_to_json(
                    {"response": CreateChat.RESPONSE_CHAT_CREATED.value, "chat_id": chat.id, "chat_name": chat_name}
                ),
            )
    return await connection.send_message(response)
