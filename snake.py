from turtle import Turtle
import time

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake():

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            snake = Turtle(shape="square")
            snake.speed(0)
            snake.color("white")
            snake.shapesize()
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)

    def move(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            new_x_position = self.snake_body[snake - 1].xcor()
            new_y_position = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(x=new_x_position, y=new_y_position)
            time.sleep(0.1)
        self.snake_body[0].forward(20)
        self.snake_body[0].right(90)
