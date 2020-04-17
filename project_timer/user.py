from dataclasses import dataclass
from random import randint


@dataclass
class User:
    """Class that stores the name and id of the user"""

    name: str
    id: int = randint(1, 100)

    def welcome(self):
        return f"Welcome{self.name}, your ID is {self.id}"


# if __name__ == "__main__":
#     user = User("Dennis")
#     print(user.id)
#     print(user.welcome())
