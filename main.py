# 0 - 2: at least 3 turtle functions
#
# 3 - 4: usage of loops
#
# 5 - 6: usage of array
#
# 7 -8: usage of recursion

import turtle

# declare turtles
# t1 draws the squares
t1 = turtle.Turtle()

# t2 draws the spiral
t2 = turtle.Turtle()

# set turtle speeds
t1.speed(15)
t2.speed(15)

# hide turtle so only the lines is shown
t1.hideturtle()
t2.hideturtle()

# the squares are orange
t1.color('orange')

# the spiral is green
t2.color('green')


def fibonacci_numb(n):
    if n < 2:
        return n
    else:
        return fibonacci_numb(n - 1) + fibonacci_numb(n - 2)


def do_fibonacci_scale(b):
    c = 0
    x = 0
    fib = fibonacci_numb(x)

    while fib < x:
        i = 0
        # create the circle
        while i < 5:
            t1.forward(c * 20)
            t1.left(90)

            i += 1

        # create a quarter circle for every square
        t2.circle(c * 20, 90)

        t1.forward(c * 20)


do_fibonacci_scale(1)


turtle.done()
