from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.highscore}",
            align="center",
            font=("Arial", 14, "bold")
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    def read_highscore(self):
        """Reads high score from a file."""
        try:
            with open("highscore.txt") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_highscore(self):
        """Saves high score to a file."""
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))
