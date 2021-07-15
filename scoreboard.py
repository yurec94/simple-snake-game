import turtle
from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 265)
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.SCORE = 0

    def add_score(self):
        self.SCORE += 1

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.SCORE}", False, align="center", font=("Courier", 24, "normal"))
