class User():
    def __init__(self, name: str, id: int):
        self.name = str(name)#CHRISTIAAN: Het lijkt me niet nodig om dit naar een string te casten. Het zou al een string moeten zijn.
        self.id = int(id)#CHRISTIAAN: Het lijkt me ook niet nodig om dit naar een int te casten.

    def welcome(self):
        if self.id < 10:
            return(f"Hello {self.name}, you have employee rights")
        if self.id >= 10:
            return(f"Hello {self.name}, you have admin rights")

    def set_timer_entry(self,TimerEntry):
        pass


    def activate_timer(self,Timer):
        pass