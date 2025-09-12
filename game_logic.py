from ascii_art import STAGES



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
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!\n")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman and guessed the word:", secret_word)
            break

        # Check loss condition
        if mistakes >= max_mistakes:
            print("Game Over! The snowman melted!")
            print("The word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        # Ignore repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter! Try another.\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print(f"Wrong guess! You have {max_mistakes - mistakes} chances left.\n")