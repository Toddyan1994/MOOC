# CalPi_MonteCarlo.py
from random import random
from time import perf_counter

DARTS = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(DARTS):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / DARTS)
print(f"圆周率值是：{pi}")
print(f"运行时间是：{perf_counter() - start:.5f}s")
