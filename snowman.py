# main.py

from game_logic import play_game

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
            play_again = input("Do you want to play again? (y/n): ").lower().strip()
            if play_again == 'y':
                break  # Exit inner loop and restart game
            elif play_again == 'n':
                print("Good Bye! Thanks for playing Snowman Meltdown!")
                return  # Exit the program
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()

