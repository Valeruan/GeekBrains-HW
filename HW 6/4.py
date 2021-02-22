class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Поехали!!')

    def stop(self):
        print(f'Остановились')

    def turn(self):
        print(f'Повернули')

    def show_speed(self):
        return int(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость для городского автомобиля превышена, сбавьте скорость')
        else:
            print(f'Это машина для города')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость для автомобиля ЖКХ превышена, сбавьте скорость')
        else:
            print(f'Это машина ЖКХ')


class SportCar(Car):
    def show_speed(self):
        if self.speed >= 120:
            print('Скорость для спорткара хорошая, но сбавьте скорость!')
        else:
            print(f'Это машина главы ЖКХ')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name, is_police)


ferrary = Car(150, "red", "Sportcar")
print(ferrary.speed)
SportCar.show_speed(ferrary)
ferrary.stop()
menty = PoliceCar(60, "blue", "ment")
print(menty.is_police)
