import turtle
from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 275)
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")
        self.SCORE = 0

    def add_score(self):
        self.SCORE += 1

    def show_score(self):
        self.clear()
        self.write(f"Score is: {self.SCORE}", False,align="center" ,font=("Arial", 16, "normal"))
