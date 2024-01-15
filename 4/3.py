# 三次样条插值
import numpy as np

# 三对角矩阵追赶法LU分解
def LU(A):
    # 获取矩阵大小
    n = A.shape[0]
    
    # 初始化 L 和 U 矩阵
    L = np.identity(n)
    U = np.zeros((n, n))
    
    # 进行分解
    for i in range(n):
        if i == 0:
            # 第一行特殊处理
            U[i][i] = A[i][i]
            U[i][i+1] = A[i][i+1]
        elif i == n-1:
            # 最后一行特殊处理
            L[i][i-1] = A[i][i-1] / U[i-1][i-1]
            U[i][i] = A[i][i] - L[i][i-1] * A[i-1][i]
        else:
            # 中间行通用处理
            L[i][i-1] = A[i][i-1] / U[i-1][i-1]
            U[i][i] = A[i][i] - L[i][i-1] * A[i-1][i]
            U[i][i+1] = A[i][i+1]
    
    return L, U

def solve(L, U, b):
    # 解下三角矩阵方程 Ly = b
    n = len(L)
    y = np.zeros(n)
    y[0] = b[0]
    for i in range(1, n):
        y[i] = b[i] - L[i][i-1] * y[i-1]
    
    # 解上三角矩阵方程 Ux = y
    x = np.zeros(n)
    x[n-1] = y[n-1] / U[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - U[i][i+1] * x[i+1]) / U[i][i]
    
    return x, y

def spline3(x, y, l, r, x0):
    n = len(x)
    h = np.zeros(n)
    for i in range(1, n):
        h[i] = x[i] - x[i - 1]

    mul = np.zeros(n)
    lam = np.zeros(n)
    for i in range(1, n - 1):
        mul[i] = h[i] / (h[i] + h[i + 1])
        lam[i] = 1 - mul[i]

    g = np.zeros(n)
    g[0] = 6 / h[1] * ((y[1] - y[0]) / h[1] - l)
    g[-1] = 6 / h[-1] * (r - (y[-1] - y[-2]) / h[-1])
    for i in range(1, n - 1):
        g[i] = 6 / (h[i] + h[i + 1]) * ((y[i + 1] - y[i]) / h[i + 1] - (y[i] - y[i - 1]) / h[i])

    d = np.zeros(n)
    d[0] = 6 * ((y[1] - y[0]) / h[1] - l) / h[1]
    d[n - 1] = 6 * (r - (y[n - 1] - y[n - 2]) / h[n - 1]) / h[n - 1]

    A = np.identity(n) * 2
    A[0][1] = 1
    A[-1][-2] = 1
    for i in range(1, n - 1):
        A[i][i - 1] = mul[i]
        A[i][i + 1] = lam[i]

    # M = np.linalg.solve(A, g)
    L, U = LU(A)
    M, _ = solve(L, U, g)

    # print(A)
    # print(g)
    # print(M)

    y0 = 0

    for i in range(n - 1):
        if x0 >= x[i] and x0 <= x[i + 1]:
            y0 += M[i] * (x[i + 1] - x0)**3 / (6 * h[i + 1]) 
            y0 += M[i + 1] * (x0 - x[i])**3 / (6 * h[i + 1]) 
            y0 += (y[i] - M[i] * h[i + 1]**2 / 6) * (x[i + 1] - x0) / h[i + 1]
            y0 += (y[i + 1] - M[i + 1] * h[i + 1]**2 / 6) * (x0 - x[i]) / h[i + 1]
            break

    return M, y0


def print_vec(b):
    for i in b:
        print(f"{i:.5f}")

if __name__ == '__main__':
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    l, r = map(float, input().split())
    x0 = float(input())
    
    M, y0 = spline3(x, y, l, r, x0)
    print_vec(M)
    print(f"{y0:.5f}")
