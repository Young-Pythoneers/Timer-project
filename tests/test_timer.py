from project_timer.timer import Timer, TimerEntry


def test_timer_creation(user):
    Timer(user.id)
    assert True


def test_timer_entry_creation(start_time, end_time, task):
    timer_entry = TimerEntry(start_time, end_time, task.id)
    assert timer_entry.start_time == start_time
    assert timer_entry.stop_time == end_time
    assert timer_entry.created_by == task
