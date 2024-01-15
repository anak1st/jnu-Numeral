import math

def fun(x):
    return math.exp(x) + 10 * x - 2

def fun2(x):
    return math.exp(x) + 10

x = 0
xx = 0
while True:
    xx = x - fun(x) / fun2(x)
    if abs(xx - x) <= 0.5e-5:
        break
    x = xx
    

print(f"{xx:.8f}")



