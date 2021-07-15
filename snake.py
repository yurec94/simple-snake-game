from turtle import Turtle  # , Screen
STARTING_POSITION = [(0, 20), (-20, 20), (-40, 20)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.body_length = 3
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            self.segments.append(turtle)
            turtle.goto(position)

    def move(self):
        self.follow_body()
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def follow_body(self):
        for part in range(len(self.segments)-1, 0, -1):
            self.segments[part].goto(self.segments[part - 1].pos())
        # if self.head.xcor() > 290 or self.head.xcor() < -300:
        #     self.restart_game()

    def add_part(self):
        body_part = Turtle(shape="square")
        body_part.penup()
        body_part.hideturtle()
        self.segments.append(body_part)
        body_part.color("white")
        body_part.showturtle()

    # def restart_game(self):
    #     Screen().reset()
    #     self.__init__()
