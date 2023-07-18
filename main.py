import time
from turtle import Screen
from Paddle import Paddle
from BALL import Ball
from scoreboard import Scoreboard
from line import Line
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.update()

r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
ball = Ball()
max_score = int(screen.textinput(title="Score",prompt="Enter MAX score"))
screen.listen()
screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)
screen.onkey(key='w', fun=l_paddle.up)
screen.onkey(key='s', fun=l_paddle.down)

score = Scoreboard()
game_is_on = True

line = Line()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    score.update_score()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.xcor() > 340 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 400:
        score.l_point()
        ball.goto(0, 0)
        ball.x_move = -15
        ball.y_move = -15

    if ball.xcor() < -400:
        score.r_point()
        ball.goto(0, 0)
        ball.x_move = 15
        ball.y_move = 15

    if score.l_score == max_score:
        score.winner("left")
        game_is_on = False

    if score.r_score == max_score:
        score.winner("right")
        game_is_on = False

screen.exitonclick()
