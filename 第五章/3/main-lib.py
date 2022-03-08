#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 样条插值
# Author: SpaceSkyNet
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
from scipy import interpolate
# plt.rcParams['font.sans-serif'] = ['Simhei']
zhfont = mpt.FontProperties(family='Simhei')

X = [520.0, 280.0, 156.6, 78.0, 39.62, 3.1, 0.0, 3.1, 39.62, 78.0, 156.6, 280, 520.0]
Y = [0.0, -30.0, -36.0, -35.0, -28.44, -9.4, 0.0, 9.4, 28.44, 35.0, 36.0, 30.0, 0.0]
N = [i + 1 for i in range(len(X))]

def fit_Xk(n):
    tck_X = interpolate.splrep(N, X, k=3)
    x = interpolate.splev(n, tck_X, der=0)

    plt.plot(N, X, 'o', n, x)
    plt.legend(['Sample Point', 'Cubic-Spline'])
    plt.xlabel('n')
    plt.ylabel('x')
    plt.title('Cubic-Spline for x[k]')
    plt.savefig('x_k Cubic-Spline-库函数.jpg')
    # plt.show()
    plt.close()
    return x

def fit_Yk(n):
    tck_Y = interpolate.splrep(N, Y, k=3)
    y = interpolate.splev(n, tck_Y, der=0)

    plt.plot(N, Y, 'o', n, y)
    plt.legend(['Sample Point', 'Cubic-Spline'])
    plt.xlabel('n')
    plt.ylabel('y')
    plt.title('Cubic-Spline for y[k]')
    plt.savefig('y_k Cubic-Spline-库函数.jpg')
    # plt.show()
    plt.close()
    return y

if __name__ == "__main__":
    assert(len(X) == len(Y))
    n = np.linspace(min(N), max(N), (len(X) - 1) ** 2)
    x = fit_Xk(n)
    y = fit_Yk(n)
    plt.figure(figsize=(15, 3))
    plt.gca().set_aspect('equal', adjustable='box') # 保证 x, y 轴比例一致
    plt.plot(x, y, X, Y, '.')
    plt.legend(['Cubic-Spline', 'Sample Point'])
    plt.axhline(y = 0,ls = ":",c = "red") # 对称轴
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('xOy平面机翼外形曲线图', fontproperties = zhfont)
    plt.savefig('xOy平面机翼外形曲线图-库函数.jpg')
    plt.show()
    plt.close()