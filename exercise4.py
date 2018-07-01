import turtle
import random

turtle.bgcolor("DarkBlue")
turtle.shape("turtle")
turtle.speed(10)

def star():
    turtle.begin_fill()
    turtle.pensize(4)
    turtle.color("yellow")
    for i in range(5):
        turtle.right(144)
        turtle.forward(20)
        turtle.left(72)
        turtle.forward(20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(random.randint(-250, 300), random.randint(-250, 300))
    turtle.pendown()

for i in range(1,30):
    star()
turtle.mainloop()
