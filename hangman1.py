import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "keyboard", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    while attempts_left > 0:
        print("\nAttempts left: {}".format(attempts_left))
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word: {}".format(current_display))

        if "_" not in current_display:
            print("Congratulations! You guessed the word: {}".format(word_to_guess))
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        if guess.isalpha() and len(guess) == 1:
            guessed_letters.append(guess)
            if guess not in word_to_guess:
                attempts_left -= 1
                print("Incorrect guess!")
        else:
            print("Invalid input. Please enter a single letter.")

    if attempts_left == 0:
        print("Sorry, you ran out of attempts. The correct word was: {}".format(word_to_guess))

if __name__ == "__main__":
    hangman()
