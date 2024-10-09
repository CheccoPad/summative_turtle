import turtle
import random
def fibonacci_turtle(it):
    # define john and his details
    john = turtle.Turtle()
    john.right(90)
    john.speed(10.1)

    # start of fib sequence
    a = 0
    b = 1

    # main fibonacci sequence calculator
    for x in range(it):
        john.color('Dark Green')
        b = a + b
        a = b - a

        # make the square
        for y in range(4):
            john.forward(b)
            john.left(90)

        # make the quarter circles
        john.circle(b, extent=90)


fibonacci_turtle(15)

turtle.Screen().exitonclick()