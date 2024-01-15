# 最小二乘拟合
import numpy as np

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
    y = np.array(list(map(float, input().split())))
    n = int(input())
    n += 1

    a = gen_coefficient_matrix(x, n)
    b = gen_right_vector(x, y, n)
    c = np.linalg.solve(a, b)
    
    print("A:")
    print_mat(a, n)
    print("b:")
    print_vec(b, n)
    print("x:")
    print_vec(c, n)
