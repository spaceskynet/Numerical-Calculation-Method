#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Guass-Legendre 数值积分求解积分方程
# Author: SpaceSkyNet
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
import math
zhfont = mpt.FontProperties(family='Simhei')

# Legendre 多项式递推公式，递归求解
def legendre_poly(n):
    if n < 2: 
        return np.eye(1, n + 1)[0]
    else:
        return np.matmul(np.array([2 * n - 1, - (n - 1)]), \
                        np.vstack((np.hstack(( legendre_poly(n - 1), 0 )), \
                                    np.hstack(( 0, 0, legendre_poly(n - 2) )) ))) / n

def calc_roots_coefs(n):
    P_n_coef = legendre_poly(n)
    P_n_derivative_coef = np.polyder(P_n_coef)
    x = np.roots(P_n_coef)
    A = np.array(list(map(lambda x_k: 2 / ((1 - x_k ** 2) * np.poly1d(P_n_derivative_coef)(x_k) ** 2), x)))
    return x, A

# y(x) = \int_l^r k(x, t)y(t)dt + f(x) , x \in [l, r]
# y(x) = (r - l) / 2 * \int_{-1}^{1} k(x, t)y(t)ds + f(x) , t = (l + r) / 2 + (r - l) / 2 * s
# y_n(x_i) = (r - l) / 2 * \sum_{j = 0}^n A_j * k(x_i, x_j) * y_n(x_j) + f(x_i), x_j = (l + r) / 2 + (r - l) / 2 * t_j (t_j 为 n 阶 Legendre 多项式零点)
# Y_n = K * W * Y_n + F --> Y_n = (I - K * W)^{-1} * F, W = (r - l) / 2 * diag(A)
def guass_fit(l, r, n, k, f):
    t, A = calc_roots_coefs(n)
    x = np.array(list(map(lambda t_i: (l + r) / 2.0 + (r - l) / 2.0 * t_i, t))) # 求积区间线性变换
    x_j, x_i = np.meshgrid(x, x)
    K = np.array(list(map(k, x_i, x_j)))
    W = (r - l) / 2.0 * np.diag(A)
    F = np.array(list(map(f, x))).T
    I = np.eye(n)
    Y = np.matmul(np.linalg.inv(I - np.matmul(K, W)), F)
    # print(I, K, W, F, x, A)
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
    l, r, n = 0, 1, 5

    # 计算求积节点及其函数近似值，作为近似表达式参数
    params = guass_fit(l, r, n, k, f)
    
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
    plt.title("Guass-Legendre 数值积分求解积分方程曲线图", fontproperties=zhfont)
    plt.legend()
    plt.savefig('Guass-Legendre 数值积分求解积分方程曲线图.jpg')
    plt.show()
    plt.close()




