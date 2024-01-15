# 牛顿型插值多项式
import math

# 差商
def diff_quotient(x, y):
    n = len(x)
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        d[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            d[i][j] = (d[i + 1][j - 1] - d[i][j - 1]) / (x[i + j] - x[i])
    return d


def calc_diff_quotient(d, x0):
    n = len(d)
    s = d[0][0]
    for i in range(1, n):
        t = 1
        for j in range(i):
            t *= (x0 - x[j])
        s += d[0][i] * t
    return s


# 差分
def diff(x, y):
    n = len(x)
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        d[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            d[i][j] = d[i + 1][j - 1] - d[i][j - 1]
    return d


def calc_diff(x, d, x0):
    n = len(d)
    s = d[0][0]
    t = 0
    for i in range(0, n):
        if x0 > x[i]:
            t = (x0 - x[i]) / (x[1] - x[0])
            break

    for i in range(1, n):
        tt = 1
        for j in range(i):
            tt *= (t - j)
        s += d[0][i] * tt / math.factorial(i)
    return s


def print_mat(mat):
    for row in mat:
        for e in row:
            print(f"{e:.5f}", end=' ')
        print()


if __name__ == '__main__':
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    x0 = float(input())

    d_fq = diff_quotient(x, y)
    y0_fq = calc_diff_quotient(d_fq, x0)
    d_ff = diff(x, y)
    y0_ff = calc_diff(x, d_ff, x0)

    print_mat(d_fq)
    print(f"{y0_fq:.5f}")
    print_mat(d_ff)
    print(f"{y0_ff:.5f}")
