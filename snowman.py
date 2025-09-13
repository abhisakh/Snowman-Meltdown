from game_logic import play_game

# ANSI colors
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def main():
    """
    Runs the full game loop and handles replay logic:
    - Calls play_game()
    - Asks the user if they want to play again after each game
    - Validates input for replay ('y' or 'n')
    """
    while True:
        play_game()

        while True:  # Nested loop to validate the user input for replay
            play_again = input(CYAN + "Do you want to play again? (y/n): " + RESET).lower().strip()
            if play_again == 'y':
                break  # Exit inner loop and restart game
            elif play_again == 'n':
                print(GREEN + "Good Bye! Thanks for playing Snowman Meltdown!" + RESET)
                return  # Exit the program
            else:
                print(RED + "Invalid input. Please enter 'y' for yes or 'n' for no." + RESET)

if __name__ == "__main__":
    main()
