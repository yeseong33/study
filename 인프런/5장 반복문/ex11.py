import turtle
t = turtle.Pen()
t.speed(-1)

for j in range(10):
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.right(30)


turtle.exitonclick()