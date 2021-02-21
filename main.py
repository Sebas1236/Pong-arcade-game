from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong: The famous Arcade Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collisions with the top and bottom walls
    # if ball.ycor() > 280 or ball.ycor() < -280
    if ball.distance(ball.xcor(), 280) < 10 or ball.distance(ball.xcor(), -280) < 10:
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    # ball.distance(-380, ball.ycor()) < 10 or ball.distance(380, ball.ycor()) < 10:
    # if ball.xcor() > 380:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
