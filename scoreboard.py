from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


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
        self.write(f"Score: {self.SCORE}",  align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        self.write("Press Space to Restart", align=ALIGNMENT, font=FONT)
        self.goto(0, -70)
        self.write("or press q to Exit", align=ALIGNMENT, font=FONT)
