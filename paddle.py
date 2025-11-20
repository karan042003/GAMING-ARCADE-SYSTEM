from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def go_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - 20)