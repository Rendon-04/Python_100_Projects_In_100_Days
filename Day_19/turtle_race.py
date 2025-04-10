from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turle = Turtle(shape='turtle')
    new_turle.color(colors[turtle_index])
    new_turle.penup()
    new_turle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('You won')
            else:
                print('You lost')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()