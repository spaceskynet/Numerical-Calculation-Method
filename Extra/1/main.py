#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 多项式最小二乘拟合
# Author: SpaceSkyNet
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
from math import floor, ceil

zhfont = mpt.FontProperties(family='Simhei')

X = [0.241, 0.615, 1.000, 1.881, 11.862, 29.457]
Y = [0.387, 0.723, 1.000, 1.524, 5.203, 9.539]

def polyld_fit(x, y, times):
    assert(len(x) == len(y))
    n, m = len(x), times
    x_pow = np.array([1 for i in range(n)])
    yx_pow = np.array(y)
    A, B = np.zeros([m + 1, m + 1]), np.zeros([m + 1, 1])
    for i in range(m + 1): # 填充正则方程组系数矩阵 A 左上三角部分及常数矩阵 B
        B[i][0] = (yx_pow * x_pow).sum()
        x_pow_sum = x_pow.sum()
        for k in range(i + 1):
            A[k][i - k] = x_pow_sum
        x_pow = x_pow * x
    for i in range(m + 1, 2 * m + 1): # 填充正则方程组系数矩阵 A 右下三角部分
        x_pow_sum = x_pow.sum()
        j = i - m
        for k in range(j, i - j + 1): # 去掉超出右下三角部分的范围
            A[k][i - k] = x_pow_sum
        x_pow = x_pow * x
    # print(A, B)
    return np.dot(np.linalg.inv(A), B).T.tolist()[0][::-1] # 解矩阵 X = inv(A) * B, 并调整格式和库函数 leastsq 输出一致

def cubic(n):
    return list(map(lambda a: a ** 3, n))

def quadratic(n):
    return list(map(lambda a: a ** 2, n))

if __name__ == "__main__":
    assert(len(X) == len(Y))
    #print(X, Y)
    fitpars = polyld_fit(quadratic(X), cubic(Y), 1)
    a, b = fitpars
    print("二次多项式拟合的最终结果为: y ** 3 = {:.6f} + {:.6f} * x ** 2".format(b, a))
    plt.figure(figsize=(20, 10))
    plt.scatter(X, Y, label="real point")

    _x = np.linspace(floor(min(X)), ceil(max(X)), 200)
    _y = list(map(lambda xi: np.poly1d(fitpars)(xi ** 2) ** (1 / 3), _x))
    plt.plot(_x, _y, label="fitting curve")
    #plt.xlim(min(X), max(X))
    plt.xlabel("x", fontproperties=zhfont)
    plt.ylabel("y", fontproperties=zhfont)
    plt.title("未知关系的x与y的多项式最小二乘拟合曲线图", fontproperties=zhfont)
    plt.legend()
    plt.savefig('未知关系的x与y的多项式最小二乘拟合曲线图.jpg')
    plt.show()
    plt.close()