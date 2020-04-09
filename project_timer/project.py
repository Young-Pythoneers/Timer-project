from dataclasses import dataclass
from typing import List

from project_timer.timer import TimerEntry
from project_timer.user import User


@dataclass
class Project:
    '''Class that stores task specific data'''
    id: str
    name: str
    created_by: User
    entries: List[TimerEntry] = List #CHRISTIAAN: ik denk dat je "= List" moet vervangen door "= []"


if __name__ == "__main__":
    user = User("Duke", 14).welcome()
    task = Project("dr", "Manhattan", user)
    print(task)
