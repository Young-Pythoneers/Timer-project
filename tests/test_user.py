import pytest
from project_timer.user import User, check_data_file, check_account_existence


@pytest.mark.parametrize("id", [2, 5, 6, 7])
def test_user_employee(id):
    cls = User(id)
    assert cls.employee_id == id


def test_data_file():
    assert check_data_file() == None
