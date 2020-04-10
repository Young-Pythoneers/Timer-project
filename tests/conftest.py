from project_timer.user import User

from datetime import datetime, timedelta
import pytest

@pytest.fixture
def start_time():
    return datetime.utcnow()

@pytest.fixture
def end_time(start_time):
    return start_time + timedelta(minutes=1)

@pytest.fixture
def user():
    return User("Dirck", 3)