import enum


class SignIn(enum.Enum):

    GET_EXISTING_USER = 'sign_in;;sender;;receiver;;token;;{"nickname": "admin", "password": "admin"}'
    GET_NON_EXISTING_USER = 'sign_in;;sender;;receiver;;token;;{"nickname": "NOTEXISTINGUSER", "password": "NOTEXISTINGPW"}'
    GET_EXISTING_USER_WRONG_PW = 'sign_in;;sender;;receiver;;token;;{"nickname": "admin", "password": "WRONG_PW"}'

    RESPONSE_CONTENT_EXISTING_USER = "SUCCESSFULLY LOGGED IN"
    RESPONSE_CONTENT_NON_EXISTING_USER = "USER NOT FOUND"
    RESPONSE_CONTENT_EXISTING_USER_WRONG_PW = "INCORRECT PASSWORD"


class SignUP(enum.Enum):

    SIGNUP_EXISTING_USER = 'sign_up;;sender;;receiver;;token;;{"nickname": "admin", "password": "admin"}'
    SIGNUP_NON_EXISTING_USER = 'sign_up;;sender;;receiver;;token;;{"nickname": "NOTEXISTINGUSER", "password": "NOTEXISTINGPW"}'
    SIGNUP_INCORRECT_PW = 'sign_up;;sender;;receiver;;token;;{"nickname": "NOTEXISTINGUSER", "password": " T"}'
    SIGNUP_INCORRECT_LOGIN = 'sign_up;;sender;;receiver;;token;;{"nickname": "_", "password": "WRONG_PW"}'

    RESPONSE_CONTENT_USER_EXISTS = "THIS LOGIN IS NOT UNIQUE"
    RESPONSE_CONTENT_SUCCESSFUL_SIGNUP = "REGISTRATION IS SUCCESSFUL"
    RESPONSE_CONTENT_INCORRECT_PW = "PASSWORD CANNOT START WITH A SPACE AND CONTAINS MORE THAN 50 CHARACTERS"
    RESPONSE_CONTENT_INCORRECT_LOGIN = "NICKNAME CANNOT START WITH A SPACE AND MUST CONTAINS ONLY 4 TO 16 CHARACTERS OF THE ENGLISH ALPHABET"


class Token(enum.Enum):

    VALID_TOKEN_LENGTH = 128
    EMPTY_TOKEN_LENGTH = 1