# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("Addictive---detail-of-Dam-007.jpg", 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle as t
import random

t.colormode(255)
color_list = [(245, 243, 237), (248, 241, 244), (238, 240, 246), (201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20)]
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(135)
tim.forward(360)
tim.setheading(0)
tim.speed("fastest")

for y in range(10):
    for i in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    tim.forward((50*10))
    tim.left(180)

screen = t.Screen()
screen.exitonclick()






