#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 样条插值
# Author: SpaceSkyNet
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
# plt.rcParams['font.sans-serif'] = ['Simhei']
zhfont = mpt.FontProperties(family='Simhei')

X = [520.0, 280.0, 156.6, 78.0, 39.62, 3.1, 0.0, 3.1, 39.62, 78.0, 156.6, 280, 520.0]
Y = [0.0, -30.0, -36.0, -35.0, -28.44, -9.4, 0.0, 9.4, 28.44, 35.0, 36.0, 30.0, 0.0]
N = [i + 1 for i in range(len(X))]

def first_boundary_condition(alpha, beta, c, n): # 追赶法求解，利用第一边值条件，取 y0' = yn' = 0
    l, u = np.zeros(n + 1), np.zeros(n + 1)
    beta[0], alpha[n] = 1, 1
    u[0] = 2
    for i in range(1, n + 1):
        l[i] = alpha[i] / u[i - 1]
        u[i] = 2 - beta[i - 1] * l[i]
    #print(l.tolist(), u.tolist())
    m, M = np.zeros(n + 1), np.zeros(n + 1)
    m[0] = c[0]
    for i in range(1, n + 1):
        m[i] = c[i] - l[i] * m[i - 1]
    M[n] = m[n] / u[n]
    for i in range(n - 1, 0 - 1, -1):
        M[i] = (m[i] - beta[i] * M[i + 1]) / u[i]
    return M

def second_boundary_condition(alpha, beta, c, n): # 追赶法求解，利用第二边值条件，取 y0'' = yn'' = 0
    l, u = np.zeros(n + 1), np.zeros(n + 1)
    u[1] = 2
    for i in range(1 + 1, n + 1 - 1):
        l[i] = alpha[i] / u[i - 1]
        u[i] = 2 - beta[i - 1] * l[i]
    #print(l.tolist(), u.tolist())
    m, M = np.zeros(n + 1), np.zeros(n + 1)
    m[1] = c[1]
    for i in range(1 + 1, n + 1 - 1):
        m[i] = c[i] - l[i] * m[i - 1]
    M[n - 1] = m[n - 1] / u[n - 1]
    for i in range(n - 1 - 1, 0 - 1 + 1, -1):
        M[i] = (m[i] - beta[i] * M[i + 1]) / u[i]
    return M

def spline_fit(x, y):
    assert(len(x) == len(y))
    n = len(x) - 1
    h, alpha, beta, c = np.zeros(n + 1), np.zeros(n + 1), np.zeros(n + 1), np.zeros(n + 1)
    A = np.zeros([n + 1, n + 1])
    for j in range(n): h[j] = x[j + 1] - x[j]
    for j in range(1, n):
        alpha[j] = h[j - 1] / (h[j - 1] + h[j])
        beta[j] = 1 - alpha[j]
        c[j] =  6 * ((y[j + 1] - y[j]) / h[j] - (y[j] - y[j - 1]) / h[j - 1]) / (h[j - 1] + h[j])
    #print(alpha.tolist(), beta.tolist(), c.tolist())
    return h, second_boundary_condition(alpha, beta, c, n) # 采用第二边值条件
  
def spline_calc(x, y, h, M, sub_x):
    assert(len(x) == len(y))
    assert(max(sub_x) <= max(X))
    now = 0
    sub_y = np.zeros(len(sub_x))
    for i in range(len(sub_x)):
        while sub_x[i] > x[now + 1]: now += 1 # 大于 x 分划的小区间右端点值
        sub_y[i] = M[now + 1] * ((sub_x[i] - x[now]) ** 3 / (6 * h[now])) - \
                   M[now] * ((sub_x[i] - x[now + 1]) ** 3 / (6 * h[now])) + \
                  (y[now + 1] - (M[now + 1] * h[now] ** 2) / 6) * (sub_x[i] - x[now]) / h[now] - \
                  (y[now] - (M[now] * h[now] ** 2) / 6) * (sub_x[i] - x[now + 1]) / h[now]
    return sub_y       


def fit_X(N, X, n):
    h, M = spline_fit(N, X)
    x = spline_calc(N, X, h, M, n)

    plt.plot(N, X, 'o', n, x)
    plt.legend(['Sample Point', 'Cubic-Spline'])
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('Cubic-Spline for x[k]')
    plt.savefig('x_k Cubic-Spline.jpg')
    # plt.show()
    plt.close()
    return x

def fit_Y(N, Y, n):
    h, M = spline_fit(N, Y)
    y = spline_calc(N, Y, h, M, n)

    plt.plot(N, Y, 'o', n, y)
    plt.legend(['Sample Point', 'Cubic-Spline'])
    plt.xlabel('n')
    plt.ylabel('y')
    plt.title('Cubic-Spline for y[k]')
    plt.savefig('y_k Cubic-Spline.jpg')
    # plt.show()
    plt.close()
    return y

if __name__ == "__main__":
    assert(len(X) == len(Y))
    n = np.linspace(min(N), max(N), (len(X) - 1) ** 2)
    x = fit_X(N, X, n)
    y = fit_Y(N, Y, n)
    plt.figure(figsize=(15, 3))
    plt.gca().set_aspect('equal', adjustable='box') # 保证 x, y 轴比例一致
    plt.plot(x, y, X, Y, '.')
    plt.legend(['Cubic-Spline', 'Sample Point'])
    plt.axhline(y = 0,ls = ":",c = "red") # 对称轴
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('xOy平面机翼外形曲线图', fontproperties = zhfont)
    plt.savefig('xOy平面机翼外形曲线图.jpg')
    plt.show()
    plt.close()