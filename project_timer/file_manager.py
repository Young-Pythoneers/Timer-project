import json
from json import JSONDecodeError
from typing import List

from project_timer.task import Task
from project_timer.timer import TimerEntry
from project_timer.user import User

""" handles all the file operations such as saving and retrieving data"""


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
WRITE_MODE = "w"
ENCODING = "utf-8"

FILENAME = "../data/data.json"


def read_data(self) -> dict:
    """tries to open data/data.json and return a dictionary of content, otherwise returns an empty dictionary"""
    data = dict

    try:
        with open(self.filename, mode=READ_MODE, encoding=ENCODING) as f:
            data = json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        with open(self.filename, mode=WRITE_MODE, encoding=ENCODING) as f:
            data["tasks"] = []
            data["entries"] = []
    return data


def save_data(self, data: dict) -> None:
    with open(FILENAME, mode=WRITE_MODE, encoding=ENCODING) as f:
        json.dump(data, f, indent=4)


class FileManager:
    """Class that handles all the file operations such as saving and retrieving data"""

    def save_task(self, task: Task) -> None:
        task_dct = task_to_dict(task)
        data = read_data()
        data["tasks"].append(task_dct)
        save_data(data)

    def get_all_tasks_by_user(self, user: User) -> List[Task]:
        """returns a list of all tasks made by a given user"""

        data = read_data()
        tasks = [
            dict_to_task(task)
            for task in data["tasks"]
            if task["usr_id"] == user.employee_id
        ]

        return tasks

    def get_all(self) -> tuple:
        """Returns a tuple of the file in a tuple containing tasks and entries"""

        data = read_data()
        tasks = [dict_to_task(task) for task in data["tasks"]]
        entries = [dict_to_entry(entry) for entry in data["entries"]]

        return tasks, entries
