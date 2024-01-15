# LU分解法求解线性方程组
import math
import numpy as np

def LU(A):
    n = A.shape[0]
    L = np.identity(n)
    U = np.zeros((n, n))
    for i in range(n):
        L[i, i] = 1
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
    return L, U

def solve(L, U, b):
    n = b.shape[0]
    y = np.zeros(n)
    x = np.zeros(n)
    # 解下三角矩阵方程 Ly = b
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    # 解上三角矩阵方程 Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    return x, y

def print_mat(A):
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            print(f"{A[i][j]:.5f}", end = ' ')
        print()

def print_vec(b):
    n = b.shape[0]
    for i in range(n):
        print(f"{b[i]:.5f}")

if __name__ == '__main__':
    # 输入矩阵
    A = list(map(float, input().split()))
    A = np.array(A)
    
    b = list(map(float, input().split()))
    b = np.array(b)

    n = int(math.sqrt(A.shape[0]))
    A = A.reshape(n, n)

    # LU 分解
    L, U = LU(A)
    # 求解
    x, y = solve(L, U, b)