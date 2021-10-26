import numpy as np


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_func(self, diff):
        a = abs(self.x ** 2 + self.y ** 2 - 1)
        b = abs(self.y - np.tan(self.x))
        return a > diff and b > diff

    def make_step(self):
        x = self.x
        y = self.y
        if abs(y) > 1:
            print('Value')
            exit(1)
        self.y = np.sqrt(1 - x ** 2)
        self.x = np.arctan(y)
        print(self.x, self.y)

    def print(self):
        print('x=', np.around(self.x, decimals=6), 'y=', np.around(self.y, decimals=6))


t = Vector(0.7, 0.7)

while t.check_func(0.000001):
    t.make_step()

t.print()
