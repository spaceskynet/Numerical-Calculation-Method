#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 分式最小二乘拟合（变形为多项式拟合）
# Author: SpaceSkyNet
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
from scipy.optimize import leastsq
zhfont = mpt.FontProperties(family='Simhei')

X = [2, 3, 5, 6, 7, 9, 10, 11, 12, 14, 16, 17, 19, 20]
Y = [106.42, 108.26, 109.58, 109.50, 109.86, 110.00, 109.93, 110.59, 110.60, 110.72, 110.90, 110.76, 111.10, 111.30]

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
    return np.dot(np.linalg.inv(A), B).T.tolist()[0] # 解矩阵 X = inv(A) * B, 并调整格式和库函数 leastsq 输出一致

def fit_func(pars, x):
    a, b = pars
    return a + b / x

if __name__ == "__main__":
    assert(len(X) == len(Y))
    X_rev = list(map(lambda xi: 1 / xi, X))
    Y_rev = list(map(lambda yi: 1 / yi, Y))
    # print(X_rev, Y_rev)
    fitpars = polyld_fit(X_rev, Y_rev, 1)
    # fitpars = fitting(X_rev, Y_rev, (0, 0))[0][::-1]
    a, b = fitpars
    print("拟合的最终结果为: 1/y = {:.6f} + {:.6f} * 1/x".format(a, b))
    plt.figure(figsize=(12, 6))
    plt.scatter(X, Y_rev, label="real point")

    _x = np.linspace(min(X), max(X), 200)
    _y_rev = list(map(lambda xi: fit_func(fitpars, xi), _x))
    # print(_x, _y)
    plt.plot(_x, _y_rev, label="fitting curve")
    plt.xlim(min(X), max(X))
    plt.xlabel("使用次数 x / 次", fontproperties=zhfont)
    plt.ylabel("容积倒数 1 / y", fontproperties=zhfont)
    plt.title("钢包容积与相应的使用次数关系拟合曲线图", fontproperties=zhfont)
    plt.legend()
    plt.savefig('钢包容积与相应的使用次数最小二乘拟合曲线图.jpg')
    plt.show()
    plt.close()