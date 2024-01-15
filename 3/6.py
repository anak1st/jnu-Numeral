import numpy as np

def inf_norm(x):
    return max(abs(x))

def GS(b):
    n = len(b)
    x0 = np.zeros(n, dtype=np.float32)
    x = x0.copy()
    for k in range(100):
        for i in range(n):
            sum = 0
            if i != 0:
                sum += -1 * x[i - 1]
            if i != n - 1:
                sum += -1 * x[i + 1]
            x[i] = (b[i] - sum) / 4
        if inf_norm(x - x0) < 1e-5:
            break
        x0 = x.copy()
    return x

if __name__ == '__main__':
    # 输入矩阵
    b = list(map(float, input().split(',')))
    b = np.array(b)
    n = b.shape[0]

    x = GS(b)
    for i in range(n):
        print(f"{x[i]:.0f}", end='' if i == n - 1 else ',')
