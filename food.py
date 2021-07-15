import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.random_position()

    def random_position(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)