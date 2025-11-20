import turtle
import random

class Pipe:
    def __init__(self, x_pos):
        self.gap = 160
        self.speed = 3

        # Top pipe
        self.top = turtle.Turtle()
        self.top.shape("square")
        self.top.shapesize(stretch_wid=20, stretch_len=3)
        self.top.color("green")
        self.top.penup()

        # Bottom pipe
        self.bottom = turtle.Turtle()
        self.bottom.shape("square")
        self.bottom.shapesize(stretch_wid=20, stretch_len=3)
        self.bottom.color("green")
        self.bottom.penup()

        self.set_position(x_pos)

    def set_position(self, x_pos):
        center = random.randint(-100, 100)
        self.top.goto(x_pos, center + self.gap/2 + 200)
        self.bottom.goto(x_pos, center - self.gap/2 - 200)

    def move(self):
        self.top.setx(self.top.xcor() - self.speed)
        self.bottom.setx(self.bottom.xcor() - self.speed)

    def off_screen(self):
        return self.top.xcor() < -400

    def reset(self):
        self.set_position(400)