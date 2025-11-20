import turtle


class Bird:
    def __init__(self):
        self.bird = turtle.Turtle()
        self.bird.shape("circle")
        self.bird.color("yellow")
        self.bird.penup()
        self.bird.goto(-100, 0)
        self.gravity = -3
        self.lift = 25
        self.velocity = 0

    def update(self):
        self.velocity += self.gravity
        new_y = self.bird.ycor() + self.velocity
        self.bird.sety(new_y)

    def flap(self):
        self.velocity = self.lift
