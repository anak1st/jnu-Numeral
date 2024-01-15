# 求 a * x^2 - b * sin(x) 极值
# 就是求 a * 2 * x - b * cos(x) = 0 的解

import math

a, b, x0 = map(float, input().split())

def fun(x):
    return a * x ** 2 - b * math.sin(x)

def fun1(x):
    return a * 2 * x - b * math.cos(x)

def fun2(x):
    return a * 2 + b * math.sin(x)

x = x0
xx = 0
while True:
    xx = x - fun1(x) / fun2(x)
    if abs(xx - x) <= 0.5e-5:
        break
    x = xx


print(f"{xx:.5f} {fun(xx):.5f}")



