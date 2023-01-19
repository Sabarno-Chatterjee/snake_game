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
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score_tracker()

    def score_tracker(self):
        self.clear()
        self.goto(x=-10, y=270)
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.current_score = 0
        self.score_tracker()
