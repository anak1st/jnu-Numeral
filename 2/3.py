# 高斯消元法求解线性方程组
import numpy as np

def gauss(a, b):
    n = b.size
    
    for i in range(n):

        for j in range(i + 1, n):
            c = a[j, i] / a[i, i]
            a[j] -= c * a[i]
            b[j] -= c * b[i]

    # print(a)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]

    return x


if __name__ == '__main__':
    s = list(map(float, input().split()))
    a = np.array(s)
    s = list(map(float, input().split()))
    b = np.array(s)
    a = a.reshape(b.size, -1)
    
    x = gauss(a, b)

    for i in x:
        print(f"{i:.5f}")