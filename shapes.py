import turtle
turtle.shape("turtle")

def triangle():
    turtle.penup()
    turtle.goto(-50, -10)
    turtle.pendown()
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    
triangle()

def square():
    turtle.penup()
    turtle.goto(100, -130)
    turtle.pendown()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)

square()

def pentagon():
    turtle.penup()
    turtle.goto(100, 150)
    turtle.pendown()
    for i in range(5):
        turtle.forward(100)
        turtle.right(72)

pentagon()

def hexagon():
    turtle.penup()
    turtle.goto(-100, 150)
    turtle.pendown()
    for i in range(6):
        turtle.forward(50)
        turtle.right(60)

hexagon()

def octagon():
    turtle.penup()
    turtle.goto(-220, 140)
    turtle.pendown()
    for i in range(8):
        turtle.forward(40)
        turtle.right(360/8)
     

octagon()

def star():
    turtle.penup()
    turtle.goto(-220, -100)
    turtle.pendown()
    for i in range(5):
        turtle.right(144)
        turtle.forward(30)
        turtle.left(72)
        turtle.forward(30)

star()

def circle():
    turtle.penup()
    turtle.goto(-90, -150)
    turtle.pendown()
    for i in range(1):
        turtle.circle(50)
        turtle.mainloop()

circle()