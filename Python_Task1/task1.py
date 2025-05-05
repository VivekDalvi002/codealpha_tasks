import random

def hangman_game():
    # List of words for the game
    word_list = ["python", "developer", "hangman", "programming", "keyboard","Hacker"]
    word_to_guess = random.choice(word_list)  # Randomly selecting a word
    guessed_word = ["_"] * len(word_to_guess)  # Initialize guessed word with underscores
    incorrect_guesses = 0
    max_attempts = 6  # Limit for incorrect guesses
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))

    while incorrect_guesses < max_attempts and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_attempts - incorrect_guesses} attempts left.")

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You've guessed the word:", word_to_guess)
    else:
        print("Game over! The word was:", word_to_guess)

hangman_game()
