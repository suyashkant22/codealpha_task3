"""Task 1: Hangman Game - CodeAlpha Python Internship"""
import random

WORDS = ["python", "variable", "function", "database", "internet"]
MAX_WRONG = 6


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word. You can make {MAX_WRONG} incorrect guesses.\n")

    while wrong < MAX_WRONG:
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print(f"Word: {display}")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print(f"Guessed letters: {', '.join(sorted(guessed)) or '-'}")

        if "_" not in display:
            print(f"\nCongratulations! You guessed '{word}'!")
            return

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
        elif guess in guessed:
            print("You already guessed that letter.\n")
        else:
            guessed.append(guess)
            if guess in word:
                print("Correct!\n")
            else:
                wrong += 1
                print("Wrong!\n")

    print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
    while True:
        play()
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break
