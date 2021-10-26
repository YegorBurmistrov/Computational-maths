import numpy as np


def func(x):
    return x * np.exp(-x**2)


# xmax = 1/sqrt(2), fmax = 1/sqrt(2e)
# eq: x * exp(-x**2) = 1/2sqrt(2e) = a
# x[k] = a * exp(x[k-1]**2)

a = 1/(2 * np.sqrt(2 * np.exp(1)))
x = np.empty(0)
x = np.append(x, 1.1)

while abs(func(x[-1]) - a) > 0.001:
    x = np.append(x, a * np.exp(x[-1]**2))

print(np.around(x, decimals=3))
print('leftx = ', x[-1])

xx = np.empty(0)
xx = np.append(xx, 1.4)

while abs(func(xx[-1]) - a) > 0.001:
    xx = np.append(xx, np.sqrt(-np.log(a/xx[-1])))

print(np.around(xx, decimals=3))
print('rightx = ', xx[-1])
print("delta = ", np.around(xx[-1] - x[-1], decimals=3))
