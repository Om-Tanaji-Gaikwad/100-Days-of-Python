FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score()

    def score(self):
        self.goto(-280,260)
        self.write(f"Level : {self.level}", font=FONT)

    def increase_level(self):
        self.clear()
        self.level+=1
        self.score()

    def game_over(self):
        new_text = Turtle()
        new_text.color("black")
        new_text.hideturtle()
        new_text.penup()
        new_text.goto(-70,0)
        new_text.write(f"Game Over!",font=FONT)