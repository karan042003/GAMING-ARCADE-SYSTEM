from turtle import Turtle, Screen
screen = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.l_score = 0
        self.r_score = 0

    def update_screen(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 80, "normal"))
        self.hideturtle()
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 80, "normal"))

    def scorein(self):
        self.l_score+=1
        self.update_screen()


    def scoreup(self):
        self.r_score+=1
        self.update_screen()