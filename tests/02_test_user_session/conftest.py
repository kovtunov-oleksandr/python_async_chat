import pytest


@pytest.fixture
def generate_user_id():
    import random

    return random.randint(99999, 999999)
