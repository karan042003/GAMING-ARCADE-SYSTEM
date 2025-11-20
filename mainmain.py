import turtle
import subprocess
import sys
import os


def show_menu():
    """Display the main menu"""
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Game Menu")

    # Create menu text
    pen = turtle.Turtle()
    pen.color("white")
    pen.hideturtle()
    pen.penup()

    # Title
    pen.goto(0, 200)
    pen.write("🎮 GAME MENU 🎮", align="center", font=("Arial", 28, "bold"))

    # Menu options
    pen.goto(0, 100)
    pen.write("1. Snake Game", align="center", font=("Arial", 18, "normal"))

    pen.goto(0, 50)
    pen.write("2. Pong Game", align="center", font=("Arial", 18, "normal"))

    pen.goto(0, 0)
    pen.write("3. Brick Breaker", align="center", font=("Arial", 18, "normal"))

    pen.goto(0, -50)
    pen.write("4. Flappy Bird", align="center", font=("Arial", 18, "normal"))

    pen.goto(0, -100)
    pen.write("5. Exit", align="center", font=("Arial", 18, "normal"))

    pen.goto(0, -180)
    pen.write("Press 1, 2, 3, 4, or 5 to select", align="center", font=("Arial", 14, "italic"))

    return screen, pen


def run_game(game_file):
    """Run a game as a separate process"""
    try:
        # Close the menu window
        turtle.bye()
    except:
        pass

    # Run the game as a subprocess and wait for it to finish
    try:
        subprocess.run([sys.executable, game_file])
    except FileNotFoundError:
        print(f"Error: Could not find {game_file}")
        input("Press Enter to return to menu...")
    except Exception as e:
        print(f"Error running game: {e}")
        input("Press Enter to return to menu...")


def main():
    """Main program loop"""
    while True:
        screen, pen = show_menu()
        choice = None

        def make_choice(num):
            nonlocal choice
            choice = num

        # Set up key bindings
        screen.listen()
        screen.onkey(lambda: make_choice(1), "1")
        screen.onkey(lambda: make_choice(2), "2")
        screen.onkey(lambda: make_choice(3), "3")
        screen.onkey(lambda: make_choice(4), "4")
        screen.onkey(lambda: make_choice(5), "5")

        # Wait for choice
        while choice is None:
            try:
                screen.update()
            except:
                # Window was closed
                sys.exit()

        # Execute choice
        if choice == 1:
            run_game("snake game.py")
        elif choice == 2:
            run_game("pongmain.py")
        elif choice == 3:
            run_game("brick_breaker (1).py")
        elif choice == 4:
            run_game("fb (1).py")
        elif choice == 5:
            print("Thanks for playing! Goodbye!")
            try:
                turtle.bye()
            except:
                pass
            sys.exit()


if __name__ == "__main__":
    main()