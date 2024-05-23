from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from grid import Grid
import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("My Pong Game")

s.tracer(0)

leftpaddle = Paddle(-350)
rightpaddle = Paddle(350)
ball = Ball(0, 0)
sboard=Scoreboard()
grid=Grid()

s.update()

s.listen()
s.onkeypress(rightpaddle.moveup, "Up")
s.onkeypress(rightpaddle.movedown, "Down")
s.onkeypress(leftpaddle.moveup, "w")
s.onkeypress(leftpaddle.movedown, "s")

gameison = True
while gameison:
    time.sleep(ball.Speed)
    s.update()
    ball.ballmove()
    if ball.distance(leftpaddle) <= 20 or ball.distance(rightpaddle) <= 20 or (
            ball.xcor() > 330 and ball.distance(rightpaddle) <= 60) or (
            ball.xcor() < -330 and ball.distance(leftpaddle) <= 60):
        ball.ballpaddlecollide()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.ballwallcollide()
    if ball.xcor() > 360:
        ball.ballreset()
        sboard.leftpaddlescore+=1
    if ball.xcor() < -360:
        ball.ballreset()
        sboard.rightpaddlescore+=1
    sboard.scoreupdate()

s.exitonclick()
