import enum


class GetMembers(enum.Enum):

    COMMAND = "get_group_members"
    RESPONSE_CHAT_NOT_FOUND = "THERE IS NO CHAT WITH ID"
    RESPONSE_LIST_RETRIEVED = "LIST OF MEMBERS RECEIVED"
