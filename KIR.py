import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def from_arr_2_funct(arr, max_x, step):
    def func(x):
        if x < max_x:
            return arr[int(x / step)]
        else:
            return arr[-1]
    return func


def calc(h, tau, max_time, max_x, y0, l_matrix, rhs):
    cur_t = 0
    cur_x = np.arange(0, max_x, h)
    cur_x = [i * h for i in range(int(max_x / h))]
    lvl_solution = y0
    solution = []
    coord_res = [[cur_t], cur_x]
    while cur_t < max_time:

        cur_lvl = calc_level(h, max_x, l_matrix, rhs, lvl_solution, cur_t)

        lvl_solution = from_arr_2_funct(cur_lvl, max_x, h)

        cur_t += tau
        coord_res[0].append(cur_t)
        solution.append(cur_lvl)
    return np.array(coord_res, dtype=object), np.array(solution)


def calc_level(h, max_x, l_matrix, rhs, lvl_solution, lvl_t):
    # level solution - func(x) a solution for t=const
    cur_x = 0
    solution = []
    while cur_x < max_x:
        if cur_x == 0:
            cur_y = lvl_solution(cur_x) - tau * l_matrix / h * (lvl_solution(cur_x + h) - lvl_solution(cur_x)) + tau * rhs(cur_x, lvl_t)
        if cur_x == max_x:
            cur_y = lvl_solution(cur_x) - tau * l_matrix / h * (lvl_solution(cur_x) - lvl_solution(cur_x - h)) + tau * rhs(cur_x, lvl_t)
        else:
            cur_y = lvl_solution(cur_x) - tau * ((l_matrix + np.absolute(l_matrix)) / (2*h) * (lvl_solution(cur_x) - lvl_solution(cur_x - h)) + (l_matrix - np.absolute(l_matrix)) / (2*h) * (lvl_solution(cur_x + h) - lvl_solution(cur_x))) + tau * rhs(cur_x, lvl_t)

        cur_x += h
        solution.append(cur_y)
    return np.array(solution)


def y0(x):
    return np.array([math.sin(x), math.cos(x)])


def rhs1(x, t):
    return np.array([0, 0])


def rhs2(x, t):
    return np.array([1, 0])


tau = 0.01
max_time = 10
h = 0.02        #Co = 1/2
max_x = math.pi

# y_0 = y0()
l_matrix = np.array([[1, 0], [0, -1]])   #lambda matrix as diag(eigenvalues)

coords, solution = calc(h, tau, max_time, max_x, y0, l_matrix, rhs1)

'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
X = coords[0]
Y = coords[1]
Z = solution
Z1 = solution[0]
Z2 = solution[1]

ax.scatter(X, Y, Z)

plt.show()
'''