import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.speed("fastest")


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b

# '''My way'''
# side = 0
#
# for i in range(1, 360):
#     tim.color(random_color())
#     tim.right(side+1)
#     tim.circle(100)

#Another way


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(1)

screen = t.Screen()
screen.exitonclick()