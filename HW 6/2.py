class Road:

    def __init__(self, lenght, width, mass):
        self._lenght = int(lenght)
        self._width = int(width)
        self._mass = int(mass)
        massa = lenght * width * mass
        print(massa)


roads = Road(int(input('Введите длину дороги - ')),
             int(input('ширину дороги - ')),
             int(input('массу асфальта для покрытия одного кв. метра дороги - ')))
