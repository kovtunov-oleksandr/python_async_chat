import pytest
import random


@pytest.fixture
def generate_user_id():
    return random.randint(99999, 999999)
