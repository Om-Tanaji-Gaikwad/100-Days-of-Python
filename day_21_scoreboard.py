from turtle import Turtle

ALLIGNMENT="center"
FONT=("Arial",24,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("day_21_data.txt","r") as file:
            highscore=file.read()
            self.highscore=int(highscore)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_score()


    def update_score(self):
        self.write(f"Score : {self.score} | High Score :{self.highscore} ", align=ALLIGNMENT, font=FONT)
    def increase_score(self):
        self.score+=1
        if self.score>self.highscore:
            with open("day_21_data.txt", "w") as file:
                file.write(str(self.score))
        with open("day_21_data.txt","r") as file:
            highscore=file.read()
            self.highscore=int(highscore)
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALLIGNMENT, font=FONT)

