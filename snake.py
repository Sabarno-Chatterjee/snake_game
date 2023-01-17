from turtle import Turtle
import time

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


def move():
    for snake in range(len(snake_body) - 1, 0, -1):
        new_x_position = snake_body[snake - 1].xcor()
        new_y_position = snake_body[snake - 1].ycor()
        snake_body[snake].goto(x=new_x_position, y=new_y_position)
        time.sleep(0.1)
    snake_body[0].forward(20)
    # snake_body[0].right(90)
