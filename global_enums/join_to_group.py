import enum


class JoinGroup(enum.Enum):

    COMMAND = "join_to_group_chat"
    RESPONSE_CHAT_NOT_FOUND = "THIS CHAT DOES NOT EXIST"
    RESPONSE_ALREADY_IN_CHAT = "YOU ARE ALREADY IN THIS CHAT"
    RESPONSE_CHAT_JOINED = "YOU JOINED THE CHAT"