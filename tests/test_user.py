import pytest
from project_timer.user import User


@pytest.mark.parametrize(
    "test_input1, test_input2", [("Henk", 3), ("Kees", 5), ("Aaron", 9), ("Lily", 1)]
)
def test_user_employee(test_input1, test_input2):
    cls = User(test_input1, test_input2)
    print(cls.welcome())
    assert cls.welcome() == f"{test_input1}, you have employee rights"


@pytest.mark.parametrize(
    "test_input1, test_input2",
    [("Dan", 14), ("Stevie", 29), ("Suzan", 31), ("Rebecca", 45)],
)
def test_user_admin(test_input1, test_input2):
    cls = User(test_input1, test_input2)
    print(cls.welcome())
    assert cls.welcome() == f"{test_input1}, you have admin rights"
