from dataclasses import dataclass
from datetime import datetime

from project_timer.user import User


@dataclass
class TimerEntry:
    """Class that stores timer data"""

    start_time: datetime
    stop_time: datetime
    task_id: int


@dataclass
class Timer:
    """Class that starts and stops a timer and returns a TimerEntry instance"""

    task_id: int
    created_by: int
    start_time: datetime = None
    stop_time: datetime = None

    def start(self):
        self.start_time = datetime.utcnow()

    def stop(self):
        self.stop_time = datetime.utcnow()
        return self.make_timer_entry()

    def make_timer_entry(self):
        return TimerEntry(self.start_time, self.stop_time, self.created_by)


if __name__ == "__main__":
    timer = Timer(User("Dirck", 3))
    timer.start()
    timer_entry = timer.stop()
    print(timer_entry.created_by.name, timer_entry.created_by.id)
    print(timer_entry.start_time, timer_entry.stop_time)
