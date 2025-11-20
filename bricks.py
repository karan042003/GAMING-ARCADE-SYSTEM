# bricks.py
from turtle import Turtle

BRICK_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(position)


class BrickManager:
    def __init__(self):
        self.bricks = []
        self.create_wall()

    def create_wall(self):
        self.bricks.clear()
        y_start = 200
        rows = 6
        cols = 10
        x_start = -260

        for row in range(rows):
            color = BRICK_COLORS[row % len(BRICK_COLORS)]
            y = y_start - row * 25
            for col in range(cols):
                x = x_start + col * 55
                brick = Brick((x, y), color)
                self.bricks.append(brick)
