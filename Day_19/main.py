from turtle import Turtle, Screen

tim = Turtle() 
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear():
    tim.reset()



screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="w", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()