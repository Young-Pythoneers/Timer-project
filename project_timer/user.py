from dataclasses import dataclass
from random import randint


@dataclass
class User:
    """Class that stores the name and id of the user"""

    name: str
    id: int = randint(1, 100)

    def welcome(self):
        if self.id < 10:
            return f"{self.name}, you have employee rights"
        if self.id >= 10:
            return f"{self.name}, you have admin rights"

    def set_timer_entry(self, TimerEntry):
        pass

    def activate_timer(self, Timer):
        pass

    def book_project(self, project):
        pass

    def book_task(self, Task):
        pass


if __name__ == "__main__":
    user = User("Dennis")
    print(user.id)
    print(user.welcome())
