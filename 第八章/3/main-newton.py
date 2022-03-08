#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Newton 法计算方程在有根区间的根
# Author: SpaceSkyNet
# [(-1.1, -1), (-0.8, -0.7), (-0.01, 0.1), (0.9, 1)]
import numpy as np

def newton_iteration(starter, phi, eps):
    print("\tx[0] = {}".format(starter))
    x, y = starter, starter + eps * 10
    iter = 0
    while abs(x - y) >= eps:
        iter += 1
        y = x
        x = phi(y)
        print("\tx[{}] = {}".format(iter, x))
    print("\t|x[{0}] - x[{1}]| = {2} < {3}, choose x[{0}]".format(iter, iter - 1, abs(x - y), eps))
    return x

def init_iterator():
    f_ceof = [0 for i in range(23 + 1)]
    f_ceof[23], f_ceof[7], f_ceof[6], f_ceof[2] = 5, -6, 8, -5
    f_ceof = np.array(f_ceof[::-1])
    f_derivative_coef = np.polyder(f_ceof)
    return lambda x: x - np.poly1d(f_ceof)(x) / np.poly1d(f_derivative_coef)(x)

if __name__ == "__main__":
    phi = init_iterator()
    eps = 1e-8
    root_interval = [(-1.1, -1), (-0.8, -0.7), (-0.01, 0.1), (0.9, 1)]
    for l, r in root_interval:
        print("({}, {}):".format(l, r))
        print("The approximate solution is {}".format(newton_iteration(l, phi, eps)))