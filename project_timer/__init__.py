from project_timer.combiner import Combiner
from project_timer.file_manager import FileManager
from project_timer.task import Task

if __name__ == "__main__":
    Combiner(input("Please enter your employee id: "))

    task = Task("coding", 765)

    file_manager = FileManager()
    file_manager.save_task(task)
