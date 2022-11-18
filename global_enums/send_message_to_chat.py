import enum


class SendMessageToChat(enum.Enum):

    COMMAND = "send_message_to_chat"
    RESPONSE_CHAT_NOT_FOUND = "THIS CHAT DOES NOT EXIST"
    RESPONSE_NOT_IN_CHAT = "YOU ARE NOT IN THIS CHAT"
    RESPONSE_MESSAGE_SENT = "MESSAGE SENT"
