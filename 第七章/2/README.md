# 第七章 数值微分与数值积分

> By: SpaceSkyNet

## 第 2 题

使用 `Python` 完成复化 Simpson 数值积分和 Guass-Legendre 数值积分求解积分方程，得到求积节点的函数近似值，（在知道精确解的情况下），采用一次多项式最小二乘近似指数函数，画出数值解和精确解及其误差的图形。

### 公式推导

设 $l = x_0 < x_1 < \cdots < x_n = r$，使用插值型积分公式有

$$
\int_l^r f(x) dx = \sum_{j = 0}^n w_j f(x_j) + R_n(x)
$$

对于第二类 Fredholm 线性积分方程，有

$$
y(x) = \int_l^r k(x, t)y(t)dt + f(x) = \sum_{j = 0}^n w_j  k(x, x_j)  y(x_j) + f(x) + R_n(x, \vec{x}), x \in [l, r], \vec{x} = (x_0, x_1, \dots, x_n)^T
$$

舍去误差项，令$y = y_n$，有

$$
y_n(x) \approx \sum_{j = 0}^n w_j  k(x, x_j)  y_n(x_j) + f(x), x \in [l, r]
$$

带入求积节点$x_i,i = 0,1, \dots, n$，有
$$
y_n(x_i) = \sum_{j = 0}^n w_j  k(x_i, x_j)  y_n(x_j) + f(x_i)
$$
令$W = diag\{w_0, w_1, \dots, w_n\}, K = (k(x_i,x_j))_{(n+1)\times(n+1)}, \\ Y_n = (y_n(x_0), \dots, y_n(x_n))^T, F_n = (f(x_0), \dots, f(x_n))^T$，将上式化为矩阵形式
$$
Y_n = KWY_n + F \\
Y_n = (I_{n+1} - KW)^{-1}F
$$
$Y_n$ 即为求积节点的函数近似值。

对于求值节点$X = (X_0,X_1,\dots,X_s)$，令$K_s = (k(X_i,x_j))_{(s+1)\times(n+1)}, F_s = (f(X_0), \dots, f(X_s))^T$，代入下面公式计算可得$Y_s$
$$
Y_s = K_s W Y_n + F_s
$$

### 复化 Simpson 数值积分

将$[l,r]$等分为$2n$份，得到$l = x_0 < x_1 < \cdots < x_{2n} = r$，令 $h = \frac{r - l}{2n}$

$$
y_n(x_i) = \frac{h}{3}(f(x_0) + f(x_{2n}) + 4\sum_{j = 0}^{n - 1} k(x_i, x_{2j + 1})y_n(x_{2j + 1}) + 2\sum_{j = 1}^{n - 1} k(x_i, x_{2j})y_n(x_{2j})) + f(x_i)
$$

则有 
$$
W = h\begin{bmatrix}
	\frac{1}{3} &             &           &      & \\
    &           \frac{4}{3}   &           &      & \\
    &           &             \frac{2}{3} &      & \\
    &           &             &           \ddots & \\
    &           &             &            &     \frac{1}{3}\\
\end{bmatrix}
$$

采用刚刚推导的矩阵形式计算$Y_n$，代入求值节点$X_s$，计算即可得$Y_s$。

经过实际操作，$(1)$小问在节点数达到 $16 \times 2 + 1 = 33$ 时，求值节点函数近似值的最大误差已经小于$10^{-6}$，十分接近精确解。

![Simpson-1]((1)\复化 Simpson 数值积分求解积分方程曲线图.jpg)

### Guass-Legendre 数值积分

$n$次勒让德多项式的递推公式为

$$
(n+1)P_{n+1}(x)=(2n+1)xP_n(x)-nP_{n-1}(x)
$$

可通过系数矩阵递归计算$n$次勒让德多项式的系数。

求出$n$次勒让德多项式的系数后，求其零点作为求积节点，求积系数$A_k = \frac{2}{(1 - x_k)[P_n'(x_k)]^2}$，对求积区间进行线性变换，有
$$
y(x) = \frac{r - l}{2}  \int_{-1}^{1} k(x, t)y(t)ds + f(x) , t = \frac{l + r}{2} + \frac{r - l}{2}s \\
y_n(x_i) = \frac{r - l}{2}  \sum_{j = 0}^n A_j  k(x_i, x_j)  y_n(x_j) + f(x_i), x_j = \frac{l + r}{2} + \frac{r - l}{2}t_j \quad (t_j 为 n 阶 Legendre 多项式零点) \\
W = \frac{r - l}{2} diag\{A_0, A_1, \dots, A_n\}
$$

由$W, x_j$计算刚刚推导的矩阵形式中的$K,W,F$，计算$Y_n$，代入求值节点$X_s$，计算即可得$Y_s$。

经过实际操作，在节点数达到 $5$ 时，求积节点函数近似值的最大误差已经小于$10^{-6}$，十分接近精确解。

![Guass-Legendre]((1)\Guass-Legendre 数值积分求解积分方程曲线图.jpg)

通过对比，在相同的误差限下，Guass-Legendre 数值积分所用的节点数少得多。

参考资料：[用复化梯形公式和外推法求解积分方程](https://www.doc88.com/p-9713380849023.html?r=1)
