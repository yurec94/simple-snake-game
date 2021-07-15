import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Simple Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
food.random_position()

screen.listen()
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
# screen.onkey(fun=snake.restart_game, key="r")

game_is_on = True
speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    score.show_score()
    if snake.head.distance(food) < 15:
        food.random_position()
        snake.add_part()
        score.add_score()
        print("test")

screen.exitonclick()
