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
t1.speed(10)
t2.speed(10)

# hide turtle so only the lines is shown
t1.hideturtle()
t2.hideturtle()

# the squares are orange
t1.color('orange')

# the spiral is green
t2.color('green')


def do_fibonacci_scale():
    b = 1
    c = 0
    user_input = int(input('how big do you want the fibonacci number to be? (Answer with and int)(8 is recommended)'))
    while c <= user_input:
        i = 0
        a = b
        b = c
        c = a + b

        # create the circle
        while i < 5:
            t1.forward(c * 20)
            t1.left(90)

            i += 1

        # create a quarter circle for every square
        t2.circle(c * 20, 90)

        t1.forward(c * 20)


do_fibonacci_scale()

turtle.done()
