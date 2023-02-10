from turtle import Screen
from pong import Pong
from ball import Ball
from score import  Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_pong = Pong((350, 0))
l_pong = Pong((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(r_pong.move_up, "Up")
screen.onkey(r_pong.move_down, "Down")
screen.onkey(l_pong.move_up, "w")
screen.onkey(l_pong.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pong) < 30 and ball.xcor() > 320 or ball.distance(l_pong) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()


screen.exitonclick()

