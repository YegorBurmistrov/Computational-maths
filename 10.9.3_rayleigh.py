import matplotlib.pyplot as plt
import numpy as np


def mpi_for_rk2(t, y, step, func):
    x = []
    x_0 = np.array([1, 1])
    x.append(x_0)
    while np.all(abs(func(t + step / 2, y + step * x[-1] / 2) - x[-1]) > 0.001):
        res = func(t + step / 2, y + step * x[-1] / 2)
        x.append(res)
    return x[-1]


def rk_2_implicit(t, y, step, func):
    k_1 = func(t + step / 2, y + step / 2)
    k_2 = mpi_for_rk2(t, y, step, func)
    return y + step * (k_1 + k_2) / 2


def eiler_implicit(t, y, step, func):
    y_res = [y + 1]
    while np.all(abs(y + step * func(t + step, y_res[-1]) - y_res[-1]) > 0.0001):
        temp = y + step * (func(t, y) + func(t + step, y_res[-1])) / 2
        y_res.append(temp)
    return y_res[-1]


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
    return np.array([y[1], 1000 * (1 - y[1] ** 2) * y[1] - y[0]])


step = 0.0001
max_time = 1000

y_0 = np.array([0, 0.001])

times_1, solution_1 = calc(y_0, step, max_time, eiler_implicit, func)

plt.scatter(times_1, solution_1[:, 0])
plt.show()
