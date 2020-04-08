from project_timer.timer import Timer, TimerEntry

def test_timer_creation():
    Timer()
    assert True

def test_timer_entry_creation():
    TimerEntry(1, 2)
    assert True