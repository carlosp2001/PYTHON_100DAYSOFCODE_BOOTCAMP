import turtle as t
import random
tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
tim.speed(0)
#
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

follow = True
i = 3
while follow:
    space = 360
    angles = space/i
    for m in range(1, i+1):
        tim.right(angles)
        tim.forward(100)
    i += 1


screen = Screen()
screen.exitonclick()
