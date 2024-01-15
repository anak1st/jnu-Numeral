import math

op = int(input())

if op == 1:
    x = 0.63212056
    for n in range(1, 15):
        x = 1 - n * x
        x = round(x, 8)
        print(f"{n}, {x:.8f}")

elif op == 2:
    x = 0.05
    for n in range(14, 0, -1):
        x = (1 - x) / n
        x = round(x, 8)
        print(f"{n - 1}, {x:.8f}")


