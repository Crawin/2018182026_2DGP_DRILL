import turtle

hor = 6
ver = 6
while (hor > 0):
    turtle.penup()
    turtle.goto(0,100 * (hor-1))
    turtle.pendown()
    turtle.forward(500)
    hor = hor - 1
turtle.left(90)
while (ver > 0):
    turtle.penup()
    turtle.goto(100*(ver-1),0)
    turtle.pendown()
    turtle.forward(500)
    ver = ver - 1


