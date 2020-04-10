from project_timer.task import Task


def test_task_creation(user):
    Task("fix code", user)
    assert True


def test_created_by(task, user):
    assert user == task.created_by


def test_id(task):
    assert 1 <= task.id & task.id <= 100  # from the randint function


def test_add_entry(task, time_entry):
    task.add_entry(time_entry)
    assert time_entry in task.entries


def test_add_entry(task, time_entry):
    task.add_entry(time_entry)
    task.remove_entry(time_entry)
    assert time_entry not in task.entries
