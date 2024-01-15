import math

def fun(x):
    return math.exp(x) + 10 * x - 2

def fun2(x):
    return (2 - math.exp(x)) / 10

x = 0
while True:
    xx = fun2(x)
    if abs(xx - x) < 5e-5:
        break
    x = xx

ans = fun(x)
print(f"{x:.5f}, {ans:.9f}")



