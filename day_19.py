# Turtle Race Game

import turtle as t
import random

colours=["red","orange","yellow","green","blue","purple"]
y_positions=[-100,-60,-20,20,60,100]
screen=t.Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make Your Bet",prompt="Which turtle colour will win ?")
all_turtles=[]
is_race_on=False

for i in range(0,6):
    kasav=t.Turtle("turtle")
    kasav.color(colours[i])
    kasav.penup()
    kasav.goto(x=-230, y=y_positions[i])
    all_turtles.append(kasav)

if user_bet:
    is_race_on=True

while is_race_on:
    for i in all_turtles:
        if i.xcor()>230:
            winner_colour=i.pencolor()
            is_race_on = False
            if winner_colour==user_bet:
                print(f"You Won!. {winner_colour} turtle is the winner.")
            else:
                print(f"You Lost!. {winner_colour} turtle is the winner.")
        random_steps = random.randint(0, 10)
        i.forward(random_steps)

screen.exitonclick()