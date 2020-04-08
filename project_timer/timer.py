from dataclasses import dataclass
from datetime import datetime

@dataclass
class TimerEntry:
    '''Class that stores timer data'''
    start_time: str
    stop_time: str

class Timer:
    '''Class that starts and stops a timer and returns a TimerEntry instance'''
    start_time: datetime
    stop_time: datetime
    def start(self):
        self.start_time = datetime.utcnow()

    def stop(self):
        self.stop_time = datetime.utcnow()
        return self.make_timer_entry()

    def make_timer_entry(self):
        start_time = self.start_time.isoformat()
        stop_time = self.stop_time.isoformat()
        return TimerEntry(start_time, stop_time)

if __name__ == "__main__":
    timer = Timer()
    timer.start()
    timer_entry = timer.stop()
    print(timer_entry.start_time, timer_entry.stop_time)