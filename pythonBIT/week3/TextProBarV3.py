import time

scale = 50
print("执行开始".center(scale // 2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print(f"\r{c:^3.0f}%[{a}->{b}]{dur:.2f}s", end="")  # \r在输出时光标返回行首
    time.sleep(0.1)
print("\n" + "执行结束".center(scale // 2, "-"))
