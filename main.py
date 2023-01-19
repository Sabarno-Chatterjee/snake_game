from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.listen()
my_screen.setup(width=600, height=600)
my_screen.title("Feed the Snake")
my_screen.bgcolor("black")
my_screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()
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
        snake.extend()
        # score.clear()
        score_board.current_score += 1
        score_board.score_tracker()
        food.refresh()

    # Detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision with tail:
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

my_screen.exitonclick()
