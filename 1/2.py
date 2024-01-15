import math

def fun(x):
    return math.exp(x) + 10 * x - 2

l = 0
r = 1

while r - l > 5e-4:
    mid = (l + r) / 2
    if fun(mid) > 0:
        r = mid
    else:
        l = mid

mid = (l + r) / 2
ans = fun(mid)
print(f"{mid:.5f}, {ans:.9f}")


