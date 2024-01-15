# 艾特肯法求解方程的根
import math

def fun(a : float, b : float, x : float):
    return a * (x ** 3) + b

def aitken(a : float, b : float, x : float):
    lastx = x
    y = x + 100
    z = x + 100
    while True:
        lastx = x
        y = fun(a, b, x)
        z = fun(a, b, y)
        x = x - (y - x) ** 2 / (z - 2 * y + x)
        # print(f"debug : {y:.6f}, {z:.6f}, {x:.6f}")
        if (abs(lastx - x) < 1e-5):
            break

    print(f"{y:.6f}, {z:.6f}, {x:.6f}")


if __name__ == "__main__":
    a, b, x = map(float, input().split())
    aitken(a, b, x)