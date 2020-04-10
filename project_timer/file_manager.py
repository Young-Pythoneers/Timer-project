class FileManager:
    """Class that handles all the file operations such as saving and retrieving data"""

    def __init__(self):
        self.filename = "data.json"
        self.filemode = "r+"  # read and write mode
        self.file = open(self.filename, self.filemode)

    def save(self, task, time) -> None:
        """takes a task name and time and save it in a file"""
        pass

    def get_time(self, task) -> float:  # float for time, can be changed later
        """takes a task and gets the times associated with that task"""
        pass

    def get_all_tasks(self) -> list:
        """returns a list of all tasks saved"""
        pass

    def get_all_tasks_and_times(self) -> tuple:  # can be changed to dictionary later
        """returns a tuple with all tasks and their times"""
        pass
