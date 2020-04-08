from dataclasses import dataclass
from typing import List

from project_timer.timer import TimerEntry
from project_timer.user import User


@dataclass
class Task:
    '''Class that stores task specific data'''
    id: str
    name: str
    created_by: User
    entries: List[TimerEntry] = List


if __name__ == "__main__":
    user = User("programmer", 1)
    task = Task("id", "fix code", user)
    print(task)
