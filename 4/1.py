# 拉格朗日插值
def lagrange(x, y, x0):
    n = len(x)
    s = 0
    for i in range(n):
        t = 1
        for j in range(n):
            if i != j:
                t *= (x0 - x[j]) / (x[i] - x[j])
        s += t * y[i]
    return s

if __name__ == '__main__':
    x = [0.0,0.1,0.195,0.3,0.401,0.5]
    y = [0.39894,0.39695,0.39142,0.38138,0.36812,0.35206]
    x0 = float(input())
    y0 = lagrange(x, y, x0)
    print(f"{y0:.5f}")
