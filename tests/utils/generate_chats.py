import secrets
import string
import random
from global_enums import CreateChat


def generate_single_valid_chat_name() -> str:
    legacy_chars = string.ascii_letters
    chat = "".join(secrets.choice(legacy_chars) for i in range(random.randint(4, 16)))
    return chat.capitalize()


def generate_single_creator_id() -> int:
    num = random.randint(1, 99999999)
    return num


def generate_type() -> int:
    num = random.randint(CreateChat.PRIVATE.value, CreateChat.PUBLIC.value)
    return num
