from turtle import Turtle, Screen
from snake import Snake

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Feed the Snake")
my_screen.bgcolor("black")
my_screen.tracer(0)

snake = Snake()
my_screen.update()
game_is_on = True

while game_is_on:
    my_screen.update()
    snake.move()


my_screen.exitonclick()
