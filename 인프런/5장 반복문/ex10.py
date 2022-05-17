# 터틀 그래픽을 활용해 별 모양을 그려보는 프로그램을 for 문을 이용해 그리기

import turtle
t = turtle.Pen()

for i in range(5):
    t.forward(120)
    t.right(140)

turtle.exitonclick()