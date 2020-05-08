# Hanoi.py
# 汉诺塔
steps = 0


def hanoi(src, des, mid, n):
    global steps
    if n == 1:
        steps += 1
        print(f"[STEP{steps:>4}]（第{n}个盘子）{src}->{des}")
    else:
        hanoi(src, mid, des, n-1)
        steps += 1
        print(f"[STEP{steps:>4}]（第{n}个盘子）{src}->{des}")
        hanoi(mid, des, src, n-1)


N = eval(input())
hanoi("A", "C", "B", N)
