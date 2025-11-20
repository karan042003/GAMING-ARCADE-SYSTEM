# brick_breaker.py
from turtle import Screen
import time
from paddle1 import Paddle
from ball1 import Ball
from bricks import BrickManager
from scoreboard1 import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Brick Breaker")
screen.tracer(0)

# Game objects
paddle = Paddle()
ball = Ball()
brick_manager = BrickManager()
scoreboard = Scoreboard()

# Key bindings
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "a")
screen.onkeypress(paddle.move_right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Collision with walls (left & right)
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    # Collision with top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # Ball misses paddle (bottom)
    if ball.ycor() < -300:
        scoreboard.lose_life()
        ball.reset_position()
        time.sleep(0.5)
        if scoreboard.lives <= 0:
            scoreboard.game_over(won=False)
            game_is_on = False

    # Collision with paddle
    if ball.ycor() < -230 and ball.ycor() > -260 and ball.distance(paddle) < 60 and ball.dy < 0:
        ball.bounce_y()

    # Collision with bricks
    for brick in brick_manager.bricks[:]:
        if ball.distance(brick) < 30:
            # Remove brick
            brick.goto(1000, 1000)
            brick_manager.bricks.remove(brick)
            scoreboard.increase_score()
            ball.bounce_y()
            break

    # Win condition (all bricks destroyed)
    if len(brick_manager.bricks) == 0:
        scoreboard.game_over(won=True)
        game_is_on = False

screen.exitonclick()
