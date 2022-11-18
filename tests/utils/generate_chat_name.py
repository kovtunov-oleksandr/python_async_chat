import string
import secrets


def generate_chat_name() -> str:
    chat_name = "".join(secrets.choice(string.ascii_letters) for i in range(10))
    return chat_name
