import turtle
import math

turtle.bgcolor("skyblue")
turtle.shape("turtle")
turtle.speed(5)

#front of house
def square():
    turtle.penup()
    turtle.goto(-100, -130)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("white")
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)
    turtle.end_fill()

square()

#door
def squaredoor():
    turtle.penup()
    turtle.goto(-90, -130)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("brown")
    for i in range(4):
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()

squaredoor()

#roof
def triangle():
    turtle.penup()
    turtle.goto(-100, 80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("brown")
    for i in range(3):
        turtle.forward(200)
        turtle.left(120)
    turtle.end_fill()
    
triangle()

#window
def squarewindow():
    turtle.penup()
    turtle.goto(30, -20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("blue")
    for i in range(4):
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()

squarewindow()

#tree base
def treebase():
    turtle.penup()
    turtle.goto(220, -90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("brown")
    for i in range(4):
        turtle.forward(30)
        turtle.left(90)
    turtle.end_fill()

treebase()

#tree
def triangle():
    turtle.penup()
    turtle.goto(180, 80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("DarkGreen")
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    
triangle()

def triangle():
    turtle.penup()
    turtle.goto(180, 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("DarkGreen")
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    
triangle()

def triangle():
    turtle.penup()
    turtle.goto(180, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(15)
    turtle.color("DarkGreen")
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()
    turtle.mainloop()
    
triangle()

