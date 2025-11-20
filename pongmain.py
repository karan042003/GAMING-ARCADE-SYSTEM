from turtle import Turtle, Screen

screen = Screen()
from scoreboard import Scoreboard
import time
from paddle import Paddle
from ball import BallTurtle

screen.listen()
l_paddle = Paddle()
l_paddle.goto(-300, 0)
ball = BallTurtle()
scoreboard = Scoreboard()
r_paddle = Paddle()
r_paddle.goto(+300, 0)

keys_pressed = {'w': False, 's': False, 'Up': False, 'Down': False}


def key_press(key):
    keys_pressed[key] = True


def key_release(key):
    keys_pressed[key] = False


screen.onkeypress(lambda: key_press('w'), "w")
screen.onkeypress(lambda: key_press('s'), "s")
screen.onkeypress(lambda: key_press('Up'), "Up")
screen.onkeypress(lambda: key_press('Down'), "Down")

screen.onkeyrelease(lambda: key_release('w'), "w")
screen.onkeyrelease(lambda: key_release('s'), "s")
screen.onkeyrelease(lambda: key_release('Up'), "Up")
screen.onkeyrelease(lambda: key_release('Down'), "Down")

while True:
    time.sleep(ball.ball_speed)
    screen.update()

    if keys_pressed['w']:
        l_paddle.go_up()
    if keys_pressed['s']:
        l_paddle.go_down()
    if keys_pressed['Up']:
        r_paddle.go_up()
    if keys_pressed['Down']:
        r_paddle.go_down()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < 230:
        ball.bounce1()

    if ball.distance(r_paddle) < 50 and ball.xcor() > -230:
        ball.bounce1()

    if ball.xcor() > 320:
        ball.reset_ball()
        scoreboard.scorein()

    if ball.xcor() < -320:
        ball.reset_ball()
        scoreboard.scoreup()

screen.exitonclick()