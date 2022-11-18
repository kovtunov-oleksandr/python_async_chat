import secrets
import string
import random


def generate_non_ascii() -> str:
    ru_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    return "".join(secrets.choice(ru_chars) for i in range(10))


def generate_invalid_login_list() -> list:
    legacy_chars = string.ascii_letters
    invalid_login = []
    for max_symbols in [3, 10, 17]:
        invalid_login.append("".join(secrets.choice(legacy_chars) for i in range(max_symbols)))
    invalid_login[1] = " " + invalid_login[1]
    invalid_login.append(generate_non_ascii())
    return invalid_login


def generate_invalid_password_list() -> list:
    legacy_chars = string.ascii_letters
    invalid_pw = []
    for max_symbols in [1, 51]:
        invalid_pw.append("".join(secrets.choice(legacy_chars) for i in range(max_symbols)))
    invalid_pw[0] = " " + invalid_pw[0]
    invalid_pw.append(generate_non_ascii())
    return invalid_pw


def generate_single_valid_login() -> str:
    legacy_chars = string.ascii_letters
    login = "".join(secrets.choice(legacy_chars) for i in range(random.randint(4, 16)))
    return login


def generate_single_valid_pw() -> str:
    legacy_chars = string.ascii_letters
    password = "".join(secrets.choice(legacy_chars) for i in range(random.randint(10, 50)))
    return password
