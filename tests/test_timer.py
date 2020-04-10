from project_timer.timer import Timer, TimerEntry


def test_timer_creation(user):
    Timer(user)
    assert True


def test_timer_entry_creation(start_time, end_time, user):
    timer_entry = TimerEntry(start_time, end_time, user)
    assert timer_entry.start_time == start_time
    assert timer_entry.stop_time == end_time
    assert timer_entry.created_by == user
