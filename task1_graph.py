import numpy as np


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_func(self, diff):
        a = abs(self.x ** 2 + self.y ** 2 - 1)
        b = abs(self.y - np.tan(self.x))
        return a > diff and b > diff

    def isCircleBigger(self, x):
        y_circle = np.sqrt(1 - x**2)
        y_tan = np.tan(x)
        return y_circle > y_tan

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

# Dixotomia
a = 0
b = 1
c = (b+a)/2
xi = []
while b - a > 0.00001:
    if t.isCircleBigger(c):
        a = c
        xi.append(c)
        c = (b + a) / 2
    elif not t.isCircleBigger(c):
        b = c
        xi.append(c)
        c = (b + a) / 2

xi.append(c)

print(np.around((c, np.tan(c)), decimals=6))

