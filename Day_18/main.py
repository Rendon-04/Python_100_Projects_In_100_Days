from turtle import Turtle, Screen, colormode
import random



colormode(255)
tim = Turtle()


tim.shape("turtle")
tim.color("#7FFF00")

# for _ in range(15):
#     tim.pencolor("black")
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# colors = ["red", "blue", "green", "purple", "black", "pink", "yellow", "orange"]

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range (3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# north, east, south, west

# def random_color():
#         r = random.randint(0,255)
#         g = random.randint(0,255)
#         b = random.randint(0,255)
#         color = (r,g,b)
#         return color

# direction = [0, 90, 198, 270]
# for _ in range(300):
#     tim.pencolor(random_color())
#     tim.pensize(10)
#     tim.speed("fast")
#     tim.forward(20)
#     tim.setheading(random.choice(direction))
    
# tim.speed("fastest")

# def draw_spiro(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.pencolor(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
    
# draw_spiro(5)

screen = Screen()
screen.exitonclick()

