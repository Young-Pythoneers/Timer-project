from project_timer.task import Task
from project_timer.timer import Timer
from project_timer.user import User, check_data_file, check_account_existence


class Combiner:
    def __init__(self, employee_id: str):
        self.id = User(employee_id)
        check_data_file()
        first_name, last_name = check_account_existence(employee_id)
        print(first_name, last_name)

    # def start_task(self, task_name: str):
    #     task = Task(task_name, self.user)
    #
    #     timer = Timer(self.user)
    #     timer.start()
    #     task.id()
    #
    # def stop_task(self, task_name: str):
    #     pass
