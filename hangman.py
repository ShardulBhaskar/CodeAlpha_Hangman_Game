import random

# List of predefined words
words = ["python", "laptop", "engineer", "cricket", "circuit"]

# Select a random word
secret_word = random.choice(words)

# Create hidden word display
display = ["_"] * len(secret_word)

# Variables
wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong_guesses and "_" in display:

    print("\nWord:", " ".join(display))
    print("Guessed Letters:", guessed_letters)
    print(f"Remaining Chances: {max_wrong_guesses - wrong_guesses}")

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("Correct!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame Over!")
    print("The word was:", secret_word)