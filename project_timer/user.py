class User():
    def __init__(self, name: str, id: int):
        self.name = str(name)
        self.id = int(id)

    def welcome(self):
        if self.id < 10:
            return(f"Hello {self.name}, you have employee rights")
        if self.id >= 10:
            return(f"Hello {self.name}, you have admin rights")

    def set_timer_entry(self,TimerEntry):
        pass


    def activate_timer(self,Timer):
        pass