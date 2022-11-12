import enum


class CreateChat(enum.Enum):

    COMMAND = "create_chat"
    RESPONSE_CHAT_NAME_EXISTS = "CHAT NAME IS NOT UNIQUE"
    RESPONSE_CHAT_CREATED = "YOU CREATED CHAT"

    USER = 0
    ADMIN = 1

    PRIVATE = 0
    PUBLIC = 1
