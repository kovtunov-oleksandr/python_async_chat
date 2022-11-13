import enum


class GetGroups(enum.Enum):

    COMMAND = "get_all_groups"
    RESPONSE_CHAT_NOT_FOUND = "THERE IS NO CHATS YET"
    RESPONSE_LIST_RETRIEVED = "LIST OF CHATS RECEIVED"
