#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 复化 Simpson 数值积分求解积分方程
# Author: SpaceSkyNet
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
import math
zhfont = mpt.FontProperties(family='Simhei')

# y(x) = \int_l^r k(x, t)y(t)dt + f(x) , x \in [l, r]
# y_n(x_i) = \sum_{j = 0}^n w_j * k(x_i, x_j) * y_n(x_j) + f(x_i)
# Y_n = K * W * Y_n + F --> Y_n = (I - K * W)^{-1} * F
def simpson_fit(l, r, n, k, f):
    h = (r - l) / (2 * n)
    x = np.linspace(l, r, 2 * n + 1)
    x_j, x_i = np.meshgrid(x, x)
    K = np.array(list(map(k, x_i, x_j)))
    W = np.zeros((2 * n + 1, 2 * n + 1))
    for i in range(n): 
        W[2 * i, 2 * i], W[2 * i + 1, 2 * i + 1] = 2 / 3, 4 / 3
    W[0, 0], W[2 * n, 2 * n] = 1 / 3, 1 / 3
    W = h * W
    F = np.array(list(map(f, x))).T
    I = np.eye(2 * n + 1)
    Y = np.matmul(np.linalg.inv(I - np.matmul(K, W)), F)
    # print(I, K, W, F)
    return (x, W, Y)

def error_calc(true_value, Y):
    errors = np.array(list(map(lambda x, y: abs(x - y), Y, true_value)))
    print("求值节点函数近似值的最大误差: {}".format(errors.max()))
    return errors

def fit_calc(X, params, k, f):
    x, W, Y = params
    x_j, x_i = np.meshgrid(x, X)
    K = np.array(list(map(k, x_i, x_j)))
    F = np.array(list(map(f, X))).T
    return K @ W @ Y + F

if __name__ == "__main__":
    k = lambda x, t: t - x
    f = lambda x: math.e ** (2 * x) + (math.e ** 2 - 1) / 2.0 * x - (math.e ** 2 + 1) / 4.0
    y = lambda x: math.e ** (2 * x)
    l, r, n = 0, 1, 16

    # 计算求积节点及其函数近似值，作为近似表达式参数
    params = simpson_fit(l, r, n, k, f)
    
    # 使用近似函数计算数值解
    _x = np.linspace(l, r, 200)
    _y = list(map(y, _x))
    _y_fit = fit_calc(_x, params, k, f)
    _errors = error_calc(_y, _y_fit)
    plt.plot(_x, _y, label="true curve")
    plt.plot(_x, _y_fit, label="fitting curve")
    plt.plot(_x, _errors, label="error curve")
    plt.xlabel("x", fontproperties=zhfont)
    plt.ylabel("y", fontproperties=zhfont)
    plt.title("复化 Simpson 数值积分求解积分方程曲线图", fontproperties=zhfont)
    plt.legend()
    plt.savefig('复化 Simpson 数值积分求解积分方程曲线图.jpg')
    plt.show()
    plt.close()
    

