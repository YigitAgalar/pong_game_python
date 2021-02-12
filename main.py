from turtle import Screen
from pong import Pong
from ball import Ball
from scoreboard import scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
screen.update()
screen.title("Pong Game")

pong1 = Pong((-350, 0))
pong2 = Pong((350, 0))
ball = Ball()

screen.listen()

screen.onkey(key="w", fun=pong1.go_up)
screen.onkey(key="s", fun=pong1.go_down)
screen.onkey(key="Up", fun=pong2.go_up)
screen.onkey(key="Down", fun=pong2.go_down)
game_is_on = True
scoreboard1 = scoreboard(1, (-350, 260))
scoreboard2 = scoreboard(2, (50, 260))
drawline=scoreboard(0, (0, 300))

drawline.draw_line()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.going()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    elif ball.xcor() <= -380:
        ball.home()
        scoreboard2.update()

    elif ball.xcor() >= 380:
        ball.home()
        scoreboard1.update()

    elif ball.distance(pong2) < 50 and ball.xcor()>320:
        ball.hit()

    elif ball.distance(pong1) < 50 and ball.xcor() < -320:
        ball.hit()

    elif scoreboard1.score >= 5:
        game_is_on = False
        drawline.clear()
        scoreboard1.game_over()
    elif scoreboard2.score >= 5:
        game_is_on = False
        drawline.clear()
        scoreboard2.game_over()




















screen.exitonclick()