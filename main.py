# 0 - 2: at least 3 turtle functions
#
# 3 - 4: usage of loops
#
# 5 - 6: usage of array
#
# 7 -8: usage of recursion
import turtle

t1 = turtle.Turtle()
# t2 = turtle.Turtle()


def fibonacci_scale(b):
    c = 0

    while c <= 4000000:
        i = 0
        a = b
        b = c
        c = a + b
        print(f' fib: {c}')

        while i < 4:
            t1.forward(c * 20)
            t1.left(90)
            print(i)
            i += 1
        t1.forward(c * 20)


fibonacci_scale(1)

turtle.done()
