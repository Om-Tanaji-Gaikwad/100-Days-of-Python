# Snake Game Part 2 (Complete Game)

from day_21_snake import Snake
from day_21_food import Food
from day_21_scoreboard import Scoreboard
from turtle import Screen
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor()> 280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()


screen.exitonclick()