#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 简单迭代法计算方程在某点附近的根
# Author: SpaceSkyNet
import math

def simple_iteration(starter, phi, eps):
    print("x[0] = {}".format(starter))
    x, y = starter, starter + eps * 10
    iter = 0
    while abs(x - y) >= eps:
        iter += 1
        y = x
        x = phi(y)
        print("x[{}] = {}".format(iter, x))
    print("|x[{0}] - x[{1}]| = {2} < {3}, choose x[{0}]".format(iter, iter - 1, abs(x - y), eps))
    return x
   
if __name__ == "__main__":
    phi = lambda x: math.e ** (-1 * x)
    eps = 1e-8
    print("The approximate solution is {}".format(simple_iteration(0.5, phi, eps)))