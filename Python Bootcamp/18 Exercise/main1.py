import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("green")
tim.speed("fastest")
tim.width(15)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


side = [0, 90, 180, 270]
for i in range(200):
    tim.color(random_color())
    tim.right(random.choice(side))
    tim.forward(30)

screen = t.Screen()
screen.exitonclick()
