#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 数值积分求考纽螺线
# Author: SpaceSkyNet
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
import math
zhfont = mpt.FontProperties(family='Simhei')

def simpson_calc(l, r, f):
    return (r - l) * (f(l) + f(r) + 4 * f((l + r) / 2.0)) / 6.0

# 选择性对半分治，满足停步准则的区间不再分治，其余区间继续分治
def quad(l, r, eps, val, f): # 多传入上次区间计算的 val 参数, 减少重复计算
    l_val, r_val = simpson_calc(l, (l + r) / 2.0, f), simpson_calc((l + r) / 2.0, r, f)
    error = l_val + r_val - val
    if abs(error) < eps * 15: # 逐次分半法停步准则
        return l_val + r_val + error / 15.0
    return quad(l, (l + r) / 2.0, eps, l_val, f) + quad((l + r) / 2.0, r, eps, r_val, f)

def x(t):
    x_eps, a = 1e-6, 1
    f = lambda t: math.cos(0.5 * a * t ** 2)
    return quad(0, t, x_eps, simpson_calc(0, t, f), f)

def y(t):
    y_eps, a = 1e-10, 1
    g = lambda t: math.sin(0.5 * a * t ** 2)
    return quad(0, t, y_eps, simpson_calc(0, t, g), g)

if __name__ == "__main__":
    L_s, R_s = -5, 5
    t = np.linspace(L_s, R_s, 200)
    X = list(map(x, t))
    Y = list(map(y, t))
    # 输出点的坐标
    print(list(map(lambda x, y: (x, y), X, Y)))
    # 画出图像
    plt.plot(X, Y)
    plt.xlabel("x", fontproperties=zhfont)
    plt.ylabel("y", fontproperties=zhfont)
    plt.title("自适应 Simpon 积分求考纽螺线图像", fontproperties=zhfont)
    plt.savefig('自适应 Simpon 积分求考纽螺线图像.jpg')
    plt.show()
    plt.close()

