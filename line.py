from turtle import  Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setheading(90)
        self.color("white")
        self.penup()
        self.fd(300)
        self.pendown()
        self.right(180)
        self.fd(600)