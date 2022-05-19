import math
import numpy as np
import matplotlib.pyplot as plt


def K(u):
    # coeff nonlinear heatpass
    alfa = 1e-2
    beta = 1e-4
    return alfa + beta * u


def calc(h, tau, max_time, y0):
    cur_t = 0
    cur_x = np.arange(0, L, h)
    # cur_x = [i * h for i in range(int(max_x / h))]
    lvl_solution = np.array([y0(i * h) for i in range(N_x)])
    solution = np.array(lvl_solution)                        # starting with y0
    coord_res = [[cur_t], cur_x]
    while cur_t < max_time:

        cur_lvl = mpi(lvl_solution)

        lvl_solution = cur_lvl        # update the level we are working on

        cur_t += tau
        coord_res[0].append(cur_t)
        solution = np.vstack((solution, cur_lvl))
    return np.array(coord_res, dtype=object), np.array(solution)


def linear_K(y_left, y_right):
    return (K(y_left) + K(y_right)) / 2


def rhs(prev_y, cur_y, next_y, interp_K):
    return (interp_K(cur_y, next_y) * (next_y - cur_y) / h - interp_K(prev_y, cur_y) * (cur_y - prev_y) / h) / h


def abs_arr(arr):
    arr_squares = [elem**2 for elem in arr]
    res = math.sqrt(np.sum(arr_squares))
    # print(res)
    return res


def mpi(prev_lvl):
    mpi_err = 0.001
    next_lvl_j = [elem + 0.001 for elem in prev_lvl]   # trash, will be deleted in 4 lines
    next_lvl_jj = prev_lvl                         # further mpi step iteration, at step 0 is equal previous level
    while abs_arr(next_lvl_j - next_lvl_jj) > mpi_err:
        # print('mpi started')
        next_lvl_j = next_lvl_jj
        for i in range(1, N_x - 1):
            '''if i == 0:
                next_lvl_jj[i] = T_left
            elif i == N_x - 1:
                next_lvl_jj[i] = T_right
            else:'''
            next_lvl_jj[i] = prev_lvl[i] + tau * rhs(next_lvl_j[i - 1], next_lvl_j[i], next_lvl_j[i + 1], linear_K)

    return next_lvl_jj


def y0(x):
    # at t=0 temperature is around 273
    T0 = 273       # mean temp in the room
    if x == 0:
        return T_left
    elif x == L - h:
        return T_right
    else:
        return T0 + math.sin(4 * math.pi * x / L)


tau = 0.01
max_time = 58
h = 0.02         # Co = 1/2
L = 10          # room size
N_x = int(L / h)  # number of dots at each level of t=const

T_left = 300      # left wall
T_right = 250     # right wall

coords, solution = calc(h, tau, max_time, y0)

fig, axs = plt.subplots(1, 4)

# y(x), time = 0
x = coords[1]
lim = int(L / h)
quarter = int(max_time / 4)
half = int(max_time / 2)
almost_final = int(max_time * 0.95)
y1 = solution[0, :lim]
y2 = solution[quarter, :lim]
y3 = solution[half, :lim]
y4 = solution[almost_final, :lim]

axs[0].plot(x, y1)
axs[0].set_title("t = 0")

axs[1].plot(x, y2)
axs[1].set_title("t = quater time")

axs[2].plot(x, y3)
axs[2].set_title("t = half time")

axs[3].plot(x, y4)
axs[3].set_title("t = final")

plt.show()
