from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score=0
        self.r_score=0
        self.update_score()
    def update_score(self):
        self.goto(0,230)
        self.write(f"Score\n{self.l_score}|{self.r_score}",align="center",font=("arial",24,"normal"))
    def increase_l_score(self):
        self.clear()
        self.l_score+=1
        self.update_score()
    def increase_r_score(self):
        self.clear()
        self.r_score+=1
        self.update_score()