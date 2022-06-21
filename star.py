import turtle

turtle.penup()
turtle.setpos(50,0)
turtle.pendown()
turtle.begin_fill()
for i in range(5):
    turtle.pencolor("blue")
    turtle.fillcolor("red")
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()
turtle.penup()
turtle.setpos(-100,0)
turtle.pendown()
turtle.begin_fill()
for i in range(5):
    #turtle.fillcolor("red","green")
    turtle.pencolor("black")
    turtle.fillcolor("green")
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()
turtle.penup()
turtle.setpos(-250,0)
turtle.pendown()
turtle.begin_fill()
for i in range(5):
    turtle.pencolor("green")
    turtle.fillcolor("orange")
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()


