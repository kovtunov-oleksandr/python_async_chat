import enum


class CreateChat(enum.Enum):

    COMMAND = "create_chat"
    RESPONSE_CHAT_NAME_EXISTS = "CHAT NAME IS NOT UNIQUE"
    RESPONSE_CHAT_CREATED = "CHAT WAS CREATED"
