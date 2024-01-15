# 最小二乘拟合
import math
import numpy as np

e = math.e

def fun(x, a, b, c, d):
    a + b * math.exp(x) + c * math.exp(-x) + d * math.exp(2 * x)

# 生成系数矩阵A
def gen_coefficient_matrix(X, n):
    a = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            a[i, j] = sum(X**(i + j))
    return a


# 计算方程组的右端向量b
def gen_right_vector(X, Y, n):
    b = np.zeros(n)
    for i in range(n):
        b[i] = sum(X**i * Y)
    return b


def print_mat(A, n):
    for i in range(n):
        for j in range(n):
            print(f"{A[i][j]:.5f}", end = ' ')
        print()

def print_vec(b, n):
    for i in range(n):
        print(f"{b[i]:.5f}")


if __name__ == '__main__':
    x = np.array(list(map(float, input().split())))
    x = np.exp(x)
    y = np.array(list(map(float, input().split())))
    for i in range(len(x)):
        y[i] /= x[i]
    n = 4

    op = int(input())

    a = gen_coefficient_matrix(x, n)
    b = gen_right_vector(x, y, n)

    A = np.zeros((n, n))

    A[0, 0] = a[0, 0]
    A[0, 1] = a[0, 1]
    A[0, 2] = a[0, 1]
    A[0, 3] = a[0, 2]
    A[1, 1] = a[0, 2]
    A[1, 2] = a[0, 0]
    A[1, 3] = a[0, 3]
    A[2, 2] = a[0, 2]
    A[2, 3] = a[0, 1]
    A[3, 3] = a[1, 3]

    for i in range(0, n):
        for j in range(0, i):
            A[i, j] = A[j, i]

    B = np.zeros(n)
    B[0] = b[1]
    B[1] = b[2]
    B[2] = b[0]
    B[3] = b[3]

    C = np.linalg.solve(A, B)

    # print_mat(a, n)

    if op == 1:
        print_mat(A, n)

    if op == 2:
        print_vec(B, n)

    if op == 3:
        print_vec(C, n)