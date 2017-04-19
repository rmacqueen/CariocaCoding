import math 
x = 3.7

while x != 1:

    if x != math.floor(x):
        x = math.floor(x)
    print x
    if x % 2 == 0:
        x = x /2
    elif x % 2 == 1:
        x = (3 * x) + 1
