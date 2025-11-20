import turtle
from bird import Bird
from pipe import Pipe

def run():

    # --------------------------- SCREEN SETUP ---------------------------
    wn = turtle.Screen()
    wn.title("Flappy Bird - Turtle Edition")
    wn.bgcolor("skyblue")
    wn.setup(width=800, height=600)
    wn.tracer(0)


    # --------------------------- START BUTTON ---------------------------
    start_button = turtle.Turtle()
    start_button.penup()
    start_button.hideturtle()
    start_button.shape("square")
    start_button.color("white")
    start_button.shapesize(stretch_wid=2, stretch_len=6)
    start_button.goto(0, -50)
    start_button.showturtle()

    # Button Text
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.color("black")
    text.goto(0, 50)
    text.write("FLAPPY BIRD", align="center", font=("Arial", 32, "bold"))

    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.color("black")
    label.goto(0, -55)
    label.write("START", align="center", font=("Arial", 20, "bold"))


    # -------------- Game will start only after button is clicked --------------
    def start_game(x, y):
        if -60 < x < 60 and -70 < y < -30:   # button hitbox
            start_button.hideturtle()
            label.clear()
            text.clear()
            start_button.clear()
            wn.onclick(None)  # disable further clicks
            begin_game()      # start the real game

    wn.onclick(start_game)


    # --------------------------- GAME FUNCTION ---------------------------
    def begin_game():
        bird = Bird()
        pipes = [Pipe(300), Pipe(600)]

        wn.listen()
        wn.onkeypress(bird.flap, "space")

        running = True

        def game_loop():
            nonlocal running

            if not running:
                return

            wn.update()
            bird.update()

            for pipe in pipes:
                pipe.move()

                if pipe.off_screen():
                    pipe.reset()

                if (bird.bird.distance(pipe.top) < 50 or
                    bird.bird.distance(pipe.bottom) < 50):
                    running = False
                    return

            if bird.bird.ycor() < -280 or bird.bird.ycor() > 280:
                running = False
                return

            wn.ontimer(game_loop, 20)

        game_loop()


    wn.mainloop()


# Prevent auto-run
if __name__ == "__main__":
    run()