from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def winner(self, win):
        self.goto(0, 0)
        self.clear()
        self.write(f"{win} is the winner", align='center', font=("Courier", 30, "normal"))