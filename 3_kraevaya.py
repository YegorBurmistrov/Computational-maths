import matplotlib.pyplot as plt
import numpy as np
import math


def rk_1(t, y, step, func):
    k_1 = func(t, y)
    return y + step * k_1


def rk_2(t, y, step, func):
    k_1 = func(t, y)
    k_2 = func(t + step / 2, y + step * k_1 / 2)
    return y + step * k_2


def rk_3(t, y, step, func):
    k_1 = func(t, y)
    k_2 = func(t + step / 3, y + step * k_1 / 3)
    k_3 = func(t + 2 * step / 3, y + step * 2 * k_2 / 3)
    return y + step / 4 * (k_1 + 3 * k_3)


def rk_4(t, y, step, func):
    k_1 = func(t, y)
    k_2 = func(t + step / 2, y + step * k_1 / 2)
    k_3 = func(t + step / 2, y + step * k_2 / 2)
    k_4 = func(t + step, y + step * k_3)
    return y + step / 6 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)


def calc(y_0, step, max_time, rk, func):
    cur_t = 0
    cur_y = y_0
    solution = [cur_y]
    times_res = [cur_t]
    while cur_t < max_time:
        cur_y = rk(cur_t, cur_y, step, func)
        cur_t += step
        times_res.append(cur_t)
        solution.append(cur_y)
    return np.array(times_res), np.array(solution)


def func(t, y):
    return np.array([y[1], (3 - t**2) * y[1] + (3 - t**2) * y[0] + 2 - 6*t + 2*t**3 + (t**2 - 3)*math.exp(t)*math.sin(t)*(1 + math.cos(t)) + math.cos(t)*(math.exp(t) + t**4 - 2*t**2 - 1)])


def func_eq(param):
    step = 0.001
    max_time = math.pi
    y_0 = np.array([0, param])

    times_1, solution_1 = calc(y_0, step, max_time, rk_4, func)
    return solution_1[:, 0][-1] - math.pi


# Dixotomia
a = 1
b = 3
c = (b+a)/2
xi = []
print(abs(func_eq(c)))
while abs(func_eq(c)) > 0.001:
    if func_eq(a) * func_eq(c) < 0:
        b = c
        xi.append(c)
        c = (b + a) / 2
    elif func_eq(b) * func_eq(c) < 0:
        a = c
        xi.append(c)
        c = (b + a) / 2
    else:
        break

xi.append(c)
print(xi, c)

step = 0.001
max_time = 1

y_0 = np.array([0, c])

times_1, solution_1 = calc(y_0, step, max_time, rk_4, func)

plt.scatter(times_1, solution_1[:, 0])
plt.show()