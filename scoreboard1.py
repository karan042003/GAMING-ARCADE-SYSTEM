# scoreboard.py
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}   Lives: {self.lives}",
            align="center",
            font=("Arial", 14, "bold")
        )

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self, won=False):
        self.goto(0, 0)
        if won:
            self.write("YOU WON! 🎉", align="center", font=("Arial", 20, "bold"))
        else:
            self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
