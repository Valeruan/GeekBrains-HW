from itertools import cycle
from time import sleep


class TrafficLight:
    __color = [['red', [7]], ['yellow', [2]], ['green', [10]], ['yellow', [2]]]

    def running(self):
        for light in cycle(self.__color):
            print(light[0][0:6])
            sleep(light[1][0])


traff = TrafficLight()
traff.running()
