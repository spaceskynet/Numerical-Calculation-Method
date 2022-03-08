#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 最小二乘拟合
# Author: SpaceSkyNet
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
from scipy.optimize import leastsq
zhfont = mpt.FontProperties(family='Simhei')

X = [2, 3, 5, 6, 7, 9, 10, 11, 12, 14, 16, 17, 19, 20]
Y = [106.42, 108.26, 109.58, 109.50, 109.86, 110.00, 109.93, 110.59, 110.60, 110.72, 110.90, 110.76, 111.10, 111.30]

def fit_func(pars, x):
    a, b = pars
    return a + b / x

def residuals(pars, x, y):
    return y - fit_func(pars, x)

def fitting(x, y, pars = (0, 0)):
    return leastsq(residuals, pars, args=(x, y))

if __name__ == "__main__":
    assert(len(X) == len(Y))
    Y_rev = list(map(lambda yi: 1/ yi, Y))    
    fitpars = fitting(X, Y_rev)[0]
    a, b = fitpars
    print("拟合的最终结果为: 1/y = {:.6f} + {:.6f} * 1/x".format(a, b))
    plt.figure(figsize=(12, 6))
    plt.scatter(X, Y_rev, label="real point")

    _x = np.linspace(min(X), max(X), 200)
    _y = list(map(lambda xi: fit_func(fitpars, xi), _x))
    plt.plot(_x, _y, label="fitting curve")
    plt.xlim(min(X), max(X))
    plt.xlabel("使用次数 x / 次", fontproperties=zhfont)
    plt.ylabel("容积倒数 1 / y", fontproperties=zhfont)
    plt.title("钢包容积与相应的使用次数关系拟合曲线图", fontproperties=zhfont)
    plt.legend()
    plt.savefig('钢包容积与相应的使用次数最小二乘拟合曲线图-库函数.jpg')
    plt.show()
    plt.close()