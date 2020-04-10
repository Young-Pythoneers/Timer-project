from dataclasses import dataclass, field
from random import randint
from typing import List

from project_timer.timer import TimerEntry
from project_timer.user import User


@dataclass
class Task:
    '''Class that stores task specific data'''
    name: str
    _created_by: User
    _id: int = randint(1, 100)
    entries: List[TimerEntry] = field(default_factory=list)

    @property
    def id(self):
        return self._id

    @property
    def created_by(self) -> User:
        return self._created_by

    def add_entry(self, entry: TimerEntry) -> None:
        self.entries.append(entry)

    def remove_entry(self, entry: TimerEntry) -> None:
        self.entries.remove(entry)


if __name__ == "__main__":
    user = User("programmer", 1)
    task = Task("fix code", user)
    print(task.created_by)
    task._created_by = User("programmer", 2)  # works and writes to _created_by
    print(task)
