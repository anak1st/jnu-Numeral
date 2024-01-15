# G-S法求解线性方程组
import numpy as np

def inf_norm(x):
    return max(abs(x))

def GS(A, b, x0):
    n = len(b)
    x = x0.copy()
    for i in range(100):
        for j in range(n):
            sum = 0
            for k in range(n):
                if k != j:
                    sum += A[j, k] * x[k]
            x[j] = (b[j] - sum) / A[j, j]
        if inf_norm(x - x0) < 1e-5:
            break
        x0 = x.copy()
    return x

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
    x0 = list(map(float, input().split()))
    x0 = np.array(x0)
    
    x = GS(A, b, x0)
    print("x:")
    print_vec(x)