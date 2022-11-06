# AICore Hangman project - Milestone 3

def ask_for_input():
    word = "banana"
    # Loop until user enters a single alphabetic character
    while True:
        guess = input("Please enter a letter: ")
        if len(guess)==1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess, word)

def check_guess(guess, word):

    # Checks whether the guess letter is contained in the randomly chosen word
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()