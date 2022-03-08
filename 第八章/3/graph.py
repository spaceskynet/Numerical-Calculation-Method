#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 作图分析方程的有根区间
# Author: SpaceSkyNet
# [(-1.1, -1), (-0.8, -0.7), (-0.01, 0.1), (0.9, 1)]
import matplotlib.pyplot as plt
import matplotlib.font_manager as mpt
import numpy as np
import math
zhfont = mpt.FontProperties(family='Simhei')

def draw_coordinate_system():
    new_ticks = np.linspace(-5, 5, 11)
    plt.yticks(new_ticks)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    yticks = ax.yaxis.get_major_ticks()
    yticks[5].label1.set_visible(False) #隐藏 y 轴的 0
    pass

def init_iterator():
    f_ceof = [0 for i in range(23 + 1)]
    f_ceof[23], f_ceof[7], f_ceof[6], f_ceof[2] = 5, -6, 8, -5
    f_ceof = np.array(f_ceof[::-1])
    return np.poly1d(f_ceof)

if __name__ == "__main__":
    f = init_iterator()
    x = np.linspace(-1.05, 1, 200)
    y = list(map(f, x))

    plt.plot(x, y)
    draw_coordinate_system()
    plt.title("作图分析方程的有根区间", fontproperties=zhfont)
    plt.savefig('作图分析方程的有根区间.jpg')
    plt.show()
    plt.close()