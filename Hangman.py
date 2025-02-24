import random

def hangman():
    """
    This function plays a text-based Hangman game.
    """
    # Create a list of words to choose from
    words = ["python", "javascript", "programming", "computer", "science"]
    # Choose a random word
    word = random.choice(words)
    # Create a list to store the guessed letters
    guessed_letters = []
    # Set the number of incorrect guesses allowed
    guesses_left = 6
    # Create a list to represent the word with underscores
    word_display = ["_"] * len(word)
    # Start the game loop
    while guesses_left > 0:
        # Print the current state of the game
        print(" ".join(word_display))
        print(f"Guesses Left: {guesses_left}")
        # Ask the player to guess a letter
        guess = input("Guess a letter: ").lower()
        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        # Add the guessed letter to the list
        guessed_letters.append(guess)
        # Check if the guess is in the word
        if guess in word:
            # Update the word display
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
            # Check if the player has won
            if "_" not in word_display:
                print(" ".join(word_display))
                print("Congratulations! You guessed the word: " + word)
                return
        else:
            # Decrement the number of guesses left
            guesses_left -= 1
            print("Incorrect guess.")
    # If the player runs out of guesses, they lose
    print("You ran out of guesses. The word was: " + word)

# Start the game
hangman()