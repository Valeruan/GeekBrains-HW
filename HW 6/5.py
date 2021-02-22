class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Вы взяли ручку. Ручка пишет.')


class Pencil(Stationery):
    def draw(self):
        print(f'Вы взяли карандаш. Карандаш рисует .')


class Handle(Stationery):
    def draw(self):
        print(f'Вы взяли маркер. Маркер выделяет и рисует.')


pen = Stationery("Ручка")
Pen.draw(pen)
pencil = Stationery("Карандаш")
Pencil.draw(pencil)
handel = Stationery("Маркер")
Handle.draw(handel)
