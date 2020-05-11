import numpy as numpy


class robot:
    def __init__(self, x=0, y=0, z=5):
        self.x = x
        self.y = y
        self.z = z

    def test1(self):

        summ = self.x + 1
        summ2 = self.y + 2 / 2
        return summ

    def test2(self):
        ave = robot.test1()
        mix = ave + self.z
        print(mix)


obj = robot()
obj.test2()
