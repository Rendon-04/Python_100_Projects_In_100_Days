import random 
from turtle import Turtle, Screen, colormode

colormode(255)

spot = Turtle()
spot.speed("fastest")
spot.penup()
spot.hideturtle()

color_list = [
    (235, 242, 248), (252, 245, 248), (28, 107, 145), (233, 151, 72), (13, 169, 208), (5, 58, 98), (29, 136, 75), (147, 77, 28), (215, 131, 162), (141, 32, 49), (215, 94, 124), (207, 156, 19), (5, 103, 66), (217, 209, 10), (2, 70, 139), (239, 213, 82), (15, 50, 45), (151, 189, 173), (120, 173, 192), (77, 85, 24), (53, 62, 17), (242, 168, 150), (233, 102, 33), (120, 54, 83), (2, 92, 122), (165, 31, 26), (213, 174, 196), (71, 158, 109)]

# starting point
spot.setheading(225)
spot.forward(300)
spot.setheading(0)

for row in range(10):
    for dot in range(10):
        spot.dot(20, random.choice(color_list))
        spot.forward(50)
    spot.setheading(90)
    spot.forward(50)
    spot.setheading(180)
    spot.forward(500)
    spot.setheading(0)





screen = Screen()
screen.exitonclick()