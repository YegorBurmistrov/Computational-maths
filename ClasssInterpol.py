import numpy as np
import matplotlib.pyplot as plt


class ClassInterpolation:
    def __init__(self, x_given, y_given):
        self.x_given = x_given
        self.y_given = y_given
        self.x = np.linspace(0, max(x_given), num=10 * max(x_given) + 1)
        self.f = np.empty(len(self.x))

    def del_dif(self, a, b):
        if isinstance(b, float) or len(b) == 1:
            return float(b)
        elif len(b) == 2:
            return (self.del_dif(a[1], b[1]) - self.del_dif(a[0], b[0]))/(a[1] - a[0])
        else:
            b_no_first = b[1:]
            a_no_first = a[1:]
            b_no_last = b[:-1]
            a_no_last = a[:-1]
            return (self.del_dif(a_no_first, b_no_first) - self.del_dif(a_no_last, b_no_last))/(a[-1] - a[0])

    # returns Pn(a)
    def polynom(self, a, xx, yy):
        result = 0

        for i in range(len(xx)):
            func = self.del_dif(xx[:len(xx)-i], yy[:len(yy)-i])

            multiplier = 1
            for j in range(len(xx) - i - 1):
                multiplier *= a - xx[j]

            # print('a=', a, 'm=', multiplier, 'f=', func, 'i=', i)
            result += func * multiplier
        return float(result)

    # Main method
    def interpolate(self):
        for i in range(len(self.x)):
            self.f[i] = self.polynom(self.x[i], self.x_given, self.y_given)

    def plot(self):
        plt.plot(self.x_given, self.y_given, 'o')

        plt.plot(self.x, self.f, '-x')

        plt.show()


# The things that we know from the very start
x_given = np.array([1, 2, 3, 4, 5, 6])
y_given = np.array([1.0, 4.0, 9.0, 16.0, 30.0, 60.0])


N = ClassInterpolation(x_given, y_given)
N.interpolate()
N.plot()
