#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 多项式最小二乘拟合
# Author: SpaceSkyNet
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
from math import floor, ceil
from scipy.optimize import leastsq
zhfont = mpt.FontProperties(family='Simhei')

X = [0.241, 0.615, 1.000, 1.881, 11.862, 29.457]
Y = [0.387, 0.723, 1.000, 1.524, 5.203, 9.539]

def residuals(pars, x, y):
    fit_func = np.poly1d(pars)
    return y - fit_func(x)

def fitting(x, y, pars):
    return leastsq(residuals, pars, args=(x, y))

if __name__ == "__main__":
    assert(len(X) == len(Y))
    print(X, Y)
    fitpars_2 = fitting(X, Y, (0, 0, 0))[0]
    a, b, c = fitpars_2
    print("二次多项式拟合的最终结果为: y = {:.6f} + {:.6f} * x + {:.6f} * x * x".format(c, b, a))
    fitpars_3 = fitting(X, Y, (0, 0, 0, 0))[0]
    a, b, c, d = fitpars_3
    print("三次多项式拟合的最终结果为: y = {:.6f} + {:.6f} * x + {:.6f} * x * x + {:.6f} * x * x * x".format(d, c, b, a))
    plt.figure(figsize=(20,10))
    plt.scatter(X, Y, label="real point")

    _x = np.linspace(floor(min(X)), ceil(max(X)), 200)
    _y_2 = list(map(lambda xi: np.poly1d(fitpars_2)(xi), _x))
    _y_3 = list(map(lambda xi: np.poly1d(fitpars_3)(xi), _x))
    plt.plot(_x, _y_2, label="Quadratic fitting curve")
    plt.plot(_x, _y_3, label="Cubic fitting curve")
    #plt.xlim(min(X), max(X))
    plt.xlabel("x", fontproperties=zhfont)
    plt.ylabel("y", fontproperties=zhfont)
    plt.title("未知关系的x与y的多项式最小二乘拟合曲线图", fontproperties=zhfont)
    plt.legend()
    plt.savefig('未知关系的x与y的多项式最小二乘拟合曲线图-库函数.jpg')
    plt.show()
    plt.close()