class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(sum(self._income.values()))


admin = Position('Sergo', 'Garz', 'Admin', 50000, 10000)
admin.get_full_name()
admin.get_total_income()
print(admin.position)
