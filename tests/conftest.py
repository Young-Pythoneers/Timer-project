from project_timer.task import Task
from project_timer.user import User
from project_timer.timer import TimerEntry

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


@pytest.fixture
def time_entry(start_time, end_time, user):
    return TimerEntry(start_time, end_time, user)


@pytest.fixture
def task(user):
    return Task("fix code", user)
