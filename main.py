import turtle as t
import random as r

colors = [(225, 158, 68), (50, 96, 57), (61, 121, 171), (240, 201, 60),  (221, 172, 199), (182, 52, 56), (174, 173, 40), (181, 64, 51), (211, 88, 56), (46, 46, 94), (209, 164, 188), (134, 160, 186), (39, 41, 80), (76, 131, 185), (148, 167, 149), (244, 199, 5), (37, 84, 46), (196, 74, 80), (228, 175, 165), (178, 188, 212), (112, 139, 114), (181, 199, 184), (32, 58, 41), (75, 143, 173), (57, 48, 38), (114, 43, 62)]

timmy = t.Turtle()
t.colormode(255)
timmy.hideturtle()
timmy.speed(0)
timmy.penup()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

total_dots = 100
for dot_count in range(1, total_dots+1):
    timmy.dot(20, r.choice(colors))
    timmy.fd(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.fd(50)
        timmy.setheading(180)
        timmy.fd(500)
        timmy.setheading(0)







t.Screen()
t.exitonclick()
# import colorgram
#
# rgb_color = []
#
# colors = colorgram.extract('spots.jpg', 30)
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

#colors = [(225, 158, 68), (50, 96, 57), (61, 121, 171), (240, 201, 60),  (221, 172, 199), (182, 52, 56), (174, 173, 40), (181, 64, 51), (211, 88, 56), (46, 46, 94), (209, 164, 188), (134, 160, 186), (39, 41, 80), (76, 131, 185), (148, 167, 149), (244, 199, 5), (37, 84, 46), (196, 74, 80), (228, 175, 165), (178, 188, 212), (112, 139, 114), (181, 199, 184), (32, 58, 41), (75, 143, 173), (57, 48, 38), (114, 43, 62)]
