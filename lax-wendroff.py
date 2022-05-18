import math
import numpy as np
import matplotlib.pyplot as plt


def calc(h, tau, max_time, max_x, y0, a, rhs):
    cur_t = 0
    cur_x = np.arange(0, max_x, h)
    cur_x = [i * h for i in range(int(max_x / h))]
    lvl_solution = [y0(i * h) for i in range(int(max_x / h))]
    solution = []
    coord_res = [[cur_t], cur_x]
    while cur_t < max_time:

        cur_lvl = calc_level(h, max_x, a, rhs, lvl_solution, cur_t)

        lvl_solution = cur_lvl

        cur_t += tau
        coord_res[0].append(cur_t)
        solution.append(cur_lvl)
    return np.array(coord_res, dtype=object), np.array(solution)


def lax_wendroff(prev_y, cur_y, next_y):
    # no rhs
    return cur_y - tau * (a / (2 * h) * (next_y - prev_y) - (a ** 2 * tau) / (2 * h ** 2) * (next_y - 2*cur_y + prev_y))


def calc_level(h, max_x, a, rhs, lvl_solution, lvl_t):
    # level solution - func(x) a solution for t=const
    solution = []
    i = 0
    N_x = int(max_x / h)
    while i < N_x:
        # print(i)
        if i == 0:
            cur_y = lax_wendroff(lvl_solution[-1], lvl_solution[0], lvl_solution[1])
        elif i == N_x - 1:
            cur_y = lax_wendroff(lvl_solution[-2], lvl_solution[-1], lvl_solution[0])
        else:
            cur_y = lax_wendroff(lvl_solution[i - 1], lvl_solution[i], lvl_solution[i + 1])

        i += 1
        solution.append(cur_y)
    return np.array(solution)


def y0(x):
    L = 20
    return math.sin(4 * math.pi * x / L)


def rhs1(x, t):
    return 0


tau = 0.01
max_time = 18   #T = 18
h = 0.02         #Co = 1/2
max_x = 20      #L = 20

a = 1

coords, solution = calc(h, tau, max_time, max_x, y0, a, rhs1)

fig, axs = plt.subplots(1, 4)

# y(x), time = 0
x = coords[1]
lim = int(max_x / h)
y1 = solution[0, :lim]
y2 = solution[50, :lim]
y3 = solution[100, :lim]
y4 = solution[150, :lim]

axs[0].plot(x, y1)
axs[0].set_title("t = 0")

axs[1].plot(x, y2)
axs[1].set_title("t = 5")

axs[2].plot(x, y3)
axs[2].set_title("t = 10")

axs[3].plot(x, y4)
axs[3].set_title("t = 15")

plt.show()
