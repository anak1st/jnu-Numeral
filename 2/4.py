# 列主元消元法求解线性方程组
import numpy as np

def print_matrix(a):
    for i in a:
        for j in i:
            print(f"{j:.5f}", end=" ")
        print()
    print()

# column pivot gauss
def gauss(a, b):
    n = b.size
    
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if abs(a[j, i]) > abs(a[k, i]):
                k = j
        if k != i:
            a[[i, k]] = a[[k, i]]
            b[[i, k]] = b[[k, i]]
        # print_matrix(a)

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