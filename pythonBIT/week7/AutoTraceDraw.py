# AutoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor('red')
t.pensize(5)

details = []
f = open('data.txt')
for line in f:
    line= line.replace()
