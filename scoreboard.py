from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 21, "normal")
TEXT = "Level:"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def increase_score(self):
        self.score += 1

    def display_score(self):
        self.penup()
        self.goto(-600, 280)
        self.write(f"{TEXT} {self.score}", align= ALIGNMENT, font= FONT)

