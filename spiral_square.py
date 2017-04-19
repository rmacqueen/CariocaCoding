import turtle
turtle.shape("turtle")

# draw a square
def make_square(turtle):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

for i in range(18):
    make_square(turtle)
    turtle.left(20)

turtle.exitonclick()