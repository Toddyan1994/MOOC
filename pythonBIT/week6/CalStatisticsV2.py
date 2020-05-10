# CalStatisticsV2.py
def getNum():  # 获取用户不定长度的输入（逗号隔开，数字至少2个）
    nums = list(eval(input()))
    return nums


def mean(numbers):  # 计算平均值
    s = 0
    for i in numbers:
        s += i/len(numbers)
    return s


def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)


def median(numbers):  # 计算中位数
    numbers = sorted(numbers)  # 或者 numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return ((numbers[n//2-1])+numbers[n//2])/2
    else:
        return numbers[n//2]


n = getNum()  # 主体函数
m = mean(n)
print(f"平均值:{m:.2f},标准差:{dev(n, m):.2f},中位数:{median(n)}")
