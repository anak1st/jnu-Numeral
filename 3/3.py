# 平方根法求解线性方程组
import numpy as np

def cholesky(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    for j in range(n):
        s = sum(L[j, k]*L[j, k] for k in range(j))
        L[j, j] = np.sqrt(A[j, j] - s)

        for i in range(j, n):
            t = sum(L[i, k]*L[j, k] for k in range(j))
            L[i, j] = (A[i, j] - t) / L[j, j]

    return L

def solve(L, b):
    n = b.shape[0]
    y = np.zeros(n)
    x = np.zeros(n)

    y[0] = b[0] / L[0][0]
    for i in range(1, n):
        y[i] = (b[i] - sum(L[i][k]*y[k] for k in range(i))) / L[i][i]

    x[n-1] = y[n-1] / L[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - sum(L[k][i]*x[k] for k in range(i+1, n))) / L[i][i]

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
    n = b.shape[0]
    A = A.reshape(n, n)
    
    L = cholesky(A)
    # 求解
    x, y = solve(L, b)

    print("L:")
    print_mat(L)
    print("y:")
    print_vec(y)
    print("x:")
    print_vec(x)
    
