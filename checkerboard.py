import turtle

turtle.shape("turtle")

length = 50

def draw_square(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()

def draw_row(cor1, cor2):
    draw_square(cor1)
    turtle.forward(length)
    draw_square(cor2)
    turtle.forward(length)
    draw_square(cor1)
    turtle.forward(length)
    draw_square(cor2)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length * 4)

draw_row("red", "black")
turtle.left(180)
draw_row("black", "red")
turtle.left(180)
draw_row("red", "black")
turtle.left(180)
draw_row("black", "red")
turtle.left(180)


turtle.mainloop()