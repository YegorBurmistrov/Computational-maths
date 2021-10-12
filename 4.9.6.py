import numpy as np
from scipy.optimize import root


def func(x, param):
    return x + np.sin(x) / 2 + param


arange = [-3, -2, -1, 1, 2, 3]

res = [root(func, 0, args=(a, )).x[0] for a in arange]

print(np.around(res, decimals=3))

# Dixotomia
param = 1
a = -10
b = 10
c = (b+a)/2
xi = []
while abs(func(c, param)) > 0.001:
    if func(a, param) * func(c, param) < 0:
        b = c
        xi.append(c)
        c = (b + a) / 2
    elif func(b, param) * func(c, param) < 0:
        a = c
        xi.append(c)
        c = (b + a) / 2
    else:
        break

xi.append(c)
print(xi, c)