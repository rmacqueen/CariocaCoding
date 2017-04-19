import turtle

def koch(order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:          # The base case is just a straight line
        turtle.forward(size)
    else:
        koch(order-1, size/3)   # Go 1/3 of the way
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)

koch(3, 300)

turtle.mainloop()