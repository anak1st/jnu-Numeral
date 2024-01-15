# 追赶法求解线性方程组
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
    # LU 分解
    L, U = LU(A)
    # 求解
    x, y = solve(L, U, b)
    print("L:")
    print_mat(L)
    print("U:")
    print_mat(U)
    print("y:")
    print_vec(y)
    print("x:")
    print_vec(x)
