from turtle import Turtle, Screen
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Feed the Snake")
my_screen.bgcolor("black")
my_screen.tracer(0)

snake_body = []


def generate_snake():
    positions = [(0, 0), (-20, 0), (-40, 0)]
    for position in positions:
        snake = Turtle(shape="square")
        snake.speed(0)
        snake.color("white")
        snake.shapesize()
        snake.penup()
        snake.goto(position)
        snake_body.append(snake)


generate_snake()
my_screen.update()
game_is_on = True

while game_is_on:
    my_screen.update()
    for snake in snake_body:
        snake.forward(20)
        time.sleep(0.1)

my_screen.exitonclick()
