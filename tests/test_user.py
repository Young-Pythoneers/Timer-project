import pytest
from project_timer.user import User


@pytest.mark.parametrize(
    "name, id", [("Henk", 3), ("Kees", 5), ("Aaron", 9), ("Lily", 1)]
)
def test_user_employee(name, id):
    cls = User(name, id)
    print(cls.welcome())
    assert cls.welcome() == f"Welcome{name}, your ID is {id}"

