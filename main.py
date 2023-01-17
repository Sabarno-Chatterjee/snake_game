from turtle import  Screen
from snake import Snake
from food import Food

my_screen = Screen()
my_screen.listen()
my_screen.setup(width=600, height=600)
my_screen.title("Feed the Snake")
my_screen.bgcolor("black")
my_screen.tracer(0)

snake = Snake()
food = Food()
my_screen.update()
my_screen.onkey(fun=snake.up, key="Up")
my_screen.onkey(fun=snake.down, key="Down")
my_screen.onkey(fun=snake.right, key="Right")
my_screen.onkey(fun=snake.left, key="Left")
game_is_on = True

while game_is_on:
    my_screen.update()
    snake.move()
    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()

my_screen.exitonclick()
