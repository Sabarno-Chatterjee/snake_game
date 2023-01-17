from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Feed the Snake")
my_screen.bgcolor("black")

snake_body = []


def generate_snake(x_position):
    for _ in range(3):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.shapesize()
        snake.goto(x=x_position, y=0)
        snake_body.append(snake)
        x_position -= 20


generate_snake(0)

my_screen.exitonclick()
