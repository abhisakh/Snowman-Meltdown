import random

STAGES = [
    """
      ___
     /___\\
     (o o)
     ( : )
     ( : )
    """,
    """
      ___
     /___\\
     (o o)
     ( : )
     (   )
    """,
    """
      ___
     /___\\
     (o o)
     (   )
     (   )
    """,
    """
      ___
     /___\\
     (o o)
         )
         )
    """,
    """
      ___
     /___\\
     (o o)

         )
    """,
    """
      ___
     /___\\
     (x x)
    """,
    """
      ___
     /___\\
    """,
    """
      ___
     /   \
    """,
]


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays current snowman stage and the guessed word so far."""
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word.strip())
    print("Guessed letters:", " ".join(guessed_letters))
    print("*"*100)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!\n")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman and guessed the word:", secret_word)
            break

        if mistakes >= max_mistakes:
            print("Game Over! The snowman melted!")
            print("The word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            if guess in secret_word:
                print("*"*100)
                print("You already guessed that letter correctly. Try another.\n")
                continue
            else:
                # Repeated wrong guess – penalize again
                mistakes += 1
                print("*"*100)
                print(f"Wrong again! You already guessed '{guess}' and it's still wrong.")
                print(f"You have {max_mistakes - mistakes} chances left.\n")
                continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("*"*100)
            print("Good guess!\n")
        else:
            mistakes += 1
            print("*"*100)
            print(f"Wrong guess! You have {max_mistakes - mistakes} chances left.\n")


def main():
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
