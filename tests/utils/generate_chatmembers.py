import random
from global_enums import CreateChat

def generate_single_user_id() -> int:
    num = random.randint(1, 99999999)
    return num


def generate_single_chat_id() -> int:
    num = random.randint(1, 99999999)
    return num


def generate_permissions() -> int:
    num = random.randint(CreateChat.PRIVATE.value, CreateChat.PUBLIC.value)
    return num
