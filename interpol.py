import numpy as np


def del_dif(x, y):
    if isinstance(y, float) or len(y) == 1:
        return float(y)
    elif len(y) == 2:
        return (del_dif(x[1], y[1]) - del_dif(x[0], y[0]))/(x[1] - x[0])
    else:
        y_no_first = y[1:]
        x_no_first = x[1:]
        y_no_last = y[:-1]
        x_no_last = x[:-1]
        return (del_dif(x_no_first, y_no_first) - del_dif(x_no_last, y_no_last))/(x[-1] - x[0])


# returns Pn(a)
def polynom(a, x_given, y_given):
    result = 0

    for i in range(len(x_given)):
        func = del_dif(x_given[:len(x_given)-i], y_given[:len(y_given)-i])

        multiplier = 1
        for j in range(len(x_given) - i - 1):
            multiplier *= a - x_given[j]

        # print('a=', a, 'm=', multiplier, 'f=', func, 'i=', i)
        result += func * multiplier
    return float(result)


# The things that we know from the very start
x_given = np.array([1, 2, 3, 4, 5, 6])
y_given = np.array([1.0, 4.0, 9.0, 16.0, 30.0, 60.0])

x = np.linspace(0, max(x_given), num=10*max(x_given)+1)
f = np.empty(len(x))
print(del_dif(x_given[:len(x_given)-1], y_given[:len(y_given)-1]))

for i in range(len(x)):
    f[i] = polynom(x[i], x_given, y_given)

# print(f)

# print(polynom(10, x_given, y_given))

import matplotlib.pyplot as plt
plt.plot(x_given, y_given, 'o')

plt.plot(x, f, '-x')

plt.show()
