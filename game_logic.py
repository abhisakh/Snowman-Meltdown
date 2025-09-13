import random
import shutil
from ascii_art import STAGES

# ANSI Color Constants
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

width = shutil.get_terminal_size().columns

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays current snowman stage and the guessed word so far."""
    print(CYAN + STAGES[mistakes] + RESET)
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += GREEN + letter + RESET + " "
        else:
            display_word += "_ "
    print(f"{BOLD}Word:{RESET}  {display_word.strip()} The secret letter has {len(secret_word)} character\n")
    print(f"{BOLD}Guessed letters:{RESET} {' '.join(guessed_letters)}\n")
    print("*" * width, "\n")


def play_game():
    """
    Handles the main gameplay loop:
    - Gets a random secret word
    - Tracks user guesses and mistakes
    - Displays the game state after each guess
    - Ends the game when the player wins or loses
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1
    print("=" * width)
    print("Welcome to Snowman Meltdown!".center(width))
    print("=" * width)

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print(GREEN + "Congratulations! You saved the snowman and guessed the word: " + secret_word + RESET)
            break

        if mistakes >= max_mistakes:
            print(RED + "Game Over! The snowman melted!" + RESET)
            print(f"The word was: {secret_word}")
            break

        guess = input("Guess a letter: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print(YELLOW + "Please enter a single valid letter.\n" + RESET)
            continue

        if guess in guessed_letters:
            if guess in secret_word:
                print("*" * width)
                print(YELLOW + "You already guessed that letter correctly. Try another.\n" + RESET)
                continue
            else:
                # Repeated wrong guess – penalize again
                mistakes += 1
                print("*" * width)
                print(RED + f"Wrong again! You already guessed '{guess}' and it's still wrong." + RESET)
                print(RED + f"You have {max_mistakes - mistakes} chances left.\n" + RESET)
                continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("*" * width)
            print(GREEN + "Good guess!\n" + RESET)
        else:
            mistakes += 1
            print("*" * width)
            print(RED + f"Wrong guess! You have {max_mistakes - mistakes} chances left.\n" + RESET)
