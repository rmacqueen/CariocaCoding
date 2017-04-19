import turtle
turtle.shape("turtle")

# draw a square
def desenha_triangulo(cor):
    turtle.color(cor)
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(136)
    turtle.forward(140)
    turtle.end_fill()

turtle.left(100)

desenha_triangulo("blue")
turtle.left(15)
desenha_triangulo("green")
turtle.left(15)
desenha_triangulo("red")
turtle.left(15)
desenha_triangulo("yellow")
turtle.left(15)
desenha_triangulo("pink")
turtle.left(15)

turtle.color('black')
turtle.left(180)
turtle.forward(180)

turtle.mainloop()