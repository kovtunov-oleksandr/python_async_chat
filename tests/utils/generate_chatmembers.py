import random


def generate_single_user_id() -> int:
    num = random.randint(9999, 99999)
    return num


def generate_single_chat_id() -> int:
    num = random.randint(9999, 99999)
    return num
