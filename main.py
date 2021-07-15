import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
SPEED = 0.1

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Simple Snake Game")
screen.tracer(0)


# screen.onkey(fun=snake.restart_game, key="r")


def start_game():
    snake = Snake()
    food = Food()
    score = Scoreboard()
    food.random_position()

    screen.listen()
    screen.onkey(fun=snake.left, key="a")
    screen.onkey(fun=snake.right, key="d")
    screen.onkey(fun=snake.up, key="w")
    screen.onkey(fun=snake.down, key="s")
    screen.onkey(fun=screen.bye, key="q")
    screen.onkey(fun=restart_game, key="space")
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(SPEED)
        snake.move()
        score.show_score()
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.random_position()
            score.add_score()
            snake.extend()
            screen.update()
        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
            game_is_on = False
            score.game_over()
        # Detect collision with snake tail
        for seg in snake.segments[1:]:
            if snake.head.distance(seg) < 15:
                game_is_on = False
                score.game_over()


def restart_game():
    screen.reset()
    start_game()


start_game()

screen.exitonclick()
