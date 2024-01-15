# 求方程全部实根和复根
import math

def fun(x : complex) -> complex:
    return x ** 4 + 2 * (x ** 3) - x - 1

def fund(x : complex) -> complex:
    return 4 * (x ** 3) + 6 * (x ** 2) - 1

def g(x : complex) -> complex:
    return x - fun(x) / fund(x)

def judge(x : complex) -> bool:
    return abs(x.real) < 1e-5 and abs(x.imag) < 1e-5

def newton_raphson(x : complex):
    cnt = 0
    while True:
        cnt += 1
        d = fund(x)
        if abs(d) < 1e-5:
            print("error")
            return
        xx = x - fun(x) / d
        if cnt > 100:
            print("error")
            return
        if judge(xx - x):
            x = xx
            break
        x = xx

    if judge(fun(x)):
        print(f"{x.real:.8f} {x.imag:.8f}i")
    else:
        print("error")
    
if __name__ == "__main__":
    x, y = map(float, input().split())
    newton_raphson(complex(x, y))
