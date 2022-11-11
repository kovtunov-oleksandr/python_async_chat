from sqlalchemy.future import select
from server.models import Chat, ChatMember
from server.server_utils.db_utils import async_session
from server.config import server
from utils.logger import logger
from utils.protocol import Message, Connection


@server.message_handler("leave_chat")
async def leave_chat(message: Message, connection: Connection):
    content = message.encode_content_from_json()
    chat_id, user_id = content["chat_id"], content["user_id"]
    logger.info(f"Attempt to leave chat {chat_id} by user_id {user_id}")
    async with async_session() as session, session.begin():
        chat_type = await session.scalar(select(Chat.type).where(Chat.id == chat_id))
        if chat_type is not None:
            if chat_type == 1:
                user_row = await session.scalar(
                    select(ChatMember).where(
                        ChatMember.chat_id == chat_id, ChatMember.user_id == user_id
                    )
                )
                if user_row:
                    await session.delete(user_row)
                    response = Message(
                        "leave_chat",
                        "server",
                        "client",
                        "_",
                        Message.decode_content_to_json(
                            {"response": "CHAT WAS LEAVED", "chat_id": chat_id}
                        ),
                    )
                else:
                    response = Message(
                        "leave_chat",
                        "server",
                        "client",
                        "_",
                        Message.decode_content_to_json(
                            {"response": "YOU ARE NOT A CHAT MEMBER"}
                        ),
                    )
            else:
                response = Message(
                    "leave_chat",
                    "server",
                    "client",
                    "_",
                    Message.decode_content_to_json(
                        {"response": "YOU CAN`T LEAVE PRIVATE CHAT"}
                    ),
                )
        else:
            response = Message(
                "leave_chat",
                "server",
                "client",
                "_",
                Message.decode_content_to_json({"response": "CHAT DAS NOT EXIST"}),
            )
        return await connection.send_message(response)
