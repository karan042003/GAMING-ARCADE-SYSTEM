# paddle.py
from turtle import Turtle

MOVE_DISTANCE = 30
PADDLE_Y = -250

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, PADDLE_Y)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x > -260:   # left boundary
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        if new_x < 260:   # right boundary
            self.goto(new_x, self.ycor())
