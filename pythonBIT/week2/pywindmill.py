# PythonDraw.py
import turtle as t

t.setup(1000, 620, 200, 200)  # 黄金分割画布
t.penup()
# t.goto(-200, -200)
t.pendown()
t.pensize(2)
t.pencolor('black')
t.seth(45)
for i in range(4):
    t.fd(150)
    t.left(90)
    t.circle(150,45)
    t.left(90)
    t.fd(150)
    t.right(135)
t.done()
