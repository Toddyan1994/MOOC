# AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor('red')
t.pensize(5)

#数据读取
datals = []
f = open(r'pythonBIT\week7\drawdata.txt')
for line in f:
    line = line.replace('\n', '')
    datals.append(list(map(eval,line.split(','))))
    #map 作用为对第二个组合数据类型所有内容应用第一个函数

# 自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()
