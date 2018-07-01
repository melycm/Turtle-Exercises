import turtle
turtle.shape("turtle")

def triangle():
    turtle.penup()
    turtle.goto(-50, -10)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("chocolate")
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    
triangle()

def square():
    turtle.penup()
    turtle.goto(100, -130)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("coral")
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

square()

def pentagon():
    turtle.penup()
    turtle.goto(100, 150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("DeepPink")
    for i in range(5):
        turtle.forward(70)
        turtle.right(72)
    turtle.end_fill()

pentagon()

def hexagon():
    turtle.penup()
    turtle.goto(-100, 150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("green")
    for i in range(6):
        turtle.forward(50)
        turtle.right(60)
    turtle.end_fill()

hexagon()

def octagon():
    turtle.penup()
    turtle.goto(-220, 140)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("blue")
    for i in range(8):
        turtle.forward(40)
        turtle.right(360/8)
    turtle.end_fill()
     

octagon()

def star():
    turtle.penup()
    turtle.goto(-220, -100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("yellow")
    for i in range(5):
        turtle.right(144)
        turtle.forward(30)
        turtle.left(72)
        turtle.forward(30)
    turtle.end_fill()

star()

def circle():
    turtle.penup()
    turtle.goto(-90, -150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("orange")
    for i in range(1):
        turtle.circle(50)
    turtle.end_fill()
    turtle.mainloop()

circle()