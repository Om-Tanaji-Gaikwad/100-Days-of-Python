# The Pong Game

from day_22_paddle import Paddle
from day_22_ball import Ball
from day_22_scoreboard import Scoreboard
from turtle import Screen
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard=Scoreboard()

ball= Ball()

screen.listen()
screen.onkey(r_paddle.up,key="Up")
screen.onkey(r_paddle.down,key="Down")
screen.onkey(l_paddle.up,key="w")
screen.onkey(l_paddle.down,key="s")

game_is_on=True
while game_is_on:
    time.sleep(ball.speed_of_ball)
    screen.update()
    ball.move_ball()
    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #detect collision with paddle
    if ball.xcor()>=320 and ball.distance(r_paddle)<50:
        ball.bounce_x()
    if ball.xcor()<=-320 and ball.distance(l_paddle)<50:
        ball.bounce_x()
    # if paddle misses
    if ball.xcor()>380:
        time.sleep(1)
        ball.reset_ball()
        scoreboard.increase_l_score()


    if ball.xcor()<-380:
        time.sleep(1)
        ball.reset_ball()
        scoreboard.increase_r_score()


screen.exitonclick()