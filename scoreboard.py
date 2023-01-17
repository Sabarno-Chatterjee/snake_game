from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.current_score = 0
        self.score_tracker()

    def score_tracker(self):
        self.goto(x=-10, y=270)
        self.write(f"Score: {self.current_score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER!", True, align=ALIGNMENT, font=FONT)
