# 0 - 2: at least 3 turtle functions
#
# 3 - 4: usage of loops
#
# 5 - 6: usage of array
#
# 7 -8: usage of recursion

import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.speed(1000)
t2.speed(1000)

t1.hideturtle()
t2.hideturtle()

t1.color('orange')
t2.color('green')


def dividing_by_2(x):
    while x > 1.0:
        x = x / 2
    return x


def dividing_by_3(x):
    while x > 1.0:
        x = x / 3
    return x


def dividing_by_4(x):
    while x > 1:
        x = x / 4
    return x


def fibonacci_scale():
    b = 1
    c = 0

    while c <= 4000000:
        i = 0
        a = b
        b = c
        c = a + b

        while i < 5:
            t1.hideturtle()
            t1.forward(c * 20)
            t1.left(90)

            i += 1

        t2.circle(c * 20, 90)

        t1.forward(c * 20)


fibonacci_scale()

turtle.done()
