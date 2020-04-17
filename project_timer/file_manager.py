import json
from typing import List

from project_timer.task import Task
from project_timer.timer import TimerEntry
from project_timer.user import User


def user_to_dict(user: User) -> dict:
    dct = dict()
    dct["name"] = user.name
    dct["id"] = user.id
    return dct


def dict_to_user(dct: dict) -> User:
    return User(dct["name"], dct["id"])


def task_to_dict(task: Task) -> dict:
    dct = dict()
    dct["name"] = task.name
    dct["id"] = task.id
    dct["usr_id"] = task.created_by
    return dct


def dict_to_task(dct: dict) -> Task:
    task = Task(dct["name"], dct["usr_id"], dct["id"])
    return task


def entry_to_dict(entry: TimerEntry) -> dict:
    dct = dict()
    dct["start_time"] = entry.start_time
    dct["stop_time"] = entry.stop_time
    dct["task_id"] = entry.task_id
    return dct


def dict_to_entry(dct: dict) -> TimerEntry:
    return TimerEntry(dct["start_time"], dct["stop_time"], dct["task_id"])


READ_WRITE_MODE = "r+"
READ_MODE = "r"
ENCODING = "utf-8"


class FileManager:
    """Class that handles all the file operations such as saving and retrieving data"""

    def __init__(self):
        self.filename = "../data/data.json"
        self.file = None

    def save(self, task: Task = None, entry: TimerEntry = None, user: User = None):
        """takes task, entry and user and saves them in a file"""
        try:
            self.file = open(self.filename, mode=READ_WRITE_MODE, encoding=ENCODING)
            data = json.load(self.file)
        except FileNotFoundError:
            data = dict()

        data["users"].append(user_to_dict(user))
        data["tasks"].append(task_to_dict(task))
        data["entries"].append(entry_to_dict(entry))

        json.dump(dict, self.file, ensure_ascii=False, indent=4)

    def get_all_tasks_by_user(self, user: User) -> List[Task]:
        """returns a list of all tasks made by a given user"""
        self.file = open(self.filename, "r", encoding="utf-8")
        data = json.load(self.file)["tasks"]
        tasks = [
            dict_to_task(task) for task in data["tasks"] if task["usr_id"] == user.id
        ]

        return tasks

    def get_all(self) -> tuple:
        """Returns a tuple of the whole file including users, tasks and entries"""
        self.file = open(self.filename, mode=READ_MODE, encoding=ENCODING)
        data = json.load(self.file)
        users = [dict_to_user(usr) for usr in data["users"]]
        tasks = [dict_to_task(task) for task in data["tasks"]]
        entries = [dict_to_entry(entry) for entry in data["entries"]]

        return users, tasks, entries


if __name__ == "__main__":
    FileManager()
