import enum


class LeaveChat(enum.Enum):

    COMMAND = "leave_chat"
    RESPONSE_NOT_CHAT_MEMBER = "YOU ARE NOT A CHAT MEMBER"
    RESPONSE_LEFT_CHAT = "YOU LEFT CHAT"
    RESPONSE_CHAT_NOT_FOUND = "THIS CHAT DOES NOT EXIST"