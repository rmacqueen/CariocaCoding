import turtle

def draw_shape (lados, comprimento, cor):
    turtle.color(cor)
    angulo = 360 / lados
    turtle.begin_fill()
    for i in range(lados):
        turtle.forward(comprimento)
        turtle.right(angulo)
    turtle.end_fill()

draw_shape(3, 80, "red")

turtle.right(90)

draw_shape(4, 80, "blue")

turtle.mainloop()