import time
from turtle import Screen
from day_23_player import Player
from day_23_car_manager import CarManager
from day_23_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
cars=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor()>280:
        player.reset_player_position()
        scoreboard.increase_level()
        cars.increase_speed()
    for car in cars.all_cars:
        if car.distance(player) < 35 and car.ycor()<player.ycor()+23 and car.ycor()>player.ycor()-20:
            scoreboard.game_over()
            game_is_on=False
    cars.generate_car()
    cars.move_cars()

screen.exitonclick()