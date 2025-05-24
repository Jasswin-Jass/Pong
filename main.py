from turtle import Screen
from paddle import Paddle
from ball import Ball
from scrore import Score
import time

sleep = 0.1

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

ball = Ball()
score = Score()

screen.update()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(sleep)
    screen.update()
    ball.move()

    # detecting collision with up and down wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 335 or ball.distance(left_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
        sleep *= 0.9

    if ball.xcor() > 380:
        time.sleep(0.6)
        ball.ball_reset()
        score.l_update()
        sleep = 0.1

    if ball.xcor() < -380:
        time.sleep(0.6)
        ball.ball_reset()
        score.r_update()
        sleep = 0.1

screen.exitonclick()
