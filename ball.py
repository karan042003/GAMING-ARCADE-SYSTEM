from turtle import Turtle,Screen
screen = Screen()
class BallTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("black")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        x=self.xcor()+self.x_move
        y=self.ycor()+self.y_move
        self.goto(x,y)

    def bounce(self):
        # self.x_move *= -1
        self.y_move *= -1
        self.ball_speed *= 0.09


    def bounce1(self):
        self.x_move *= -1
        # self.y_move *= -1
        self.ball_speed *= 0.09



    def reset_ball(self):
        screen.update()
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce1()