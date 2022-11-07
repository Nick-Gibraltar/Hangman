# AICore Project 1 - Hangman
import random

class Hangman:

        def __init__(self, word_list, num_lives=5):

            self.word_list = word_list                  # List containing the possible words
            self.num_lives = num_lives                  # Number of lives
            self.word = random.choice(word_list)        # The actual word to be guessed chosen from word_list
            self.num_letters = len(self.word)           # Number of letters in the word
            self.list_of_guesses = []                   # List to store the letters already guessed
            self.word_guessed = len(self.word) * ["_"]  # Represents the partially guessed word        

        def check_guess(self, guess):

            if guess in self.word:                  # If the target word contains the guessed letter
                print(f"Good guess! {guess} is in the word.")
                for i, j in enumerate(self.word):   # Iterate through the target word 
                    if guess==j:                    # And set the elements of word_guessed to be equal
                        self.word_guessed[i]=j      # to the guessed letter in the appropriate place
                        self.num_letters -=1
            else:
                self.num_lives -=1                  # If it's not, then lose a life and print a message
                print(f"Sorry, {guess} is not in the word.")
                print(f"You have {self.num_lives} lives left.")


        def ask_for_input(self):

            while True:
                # Print a message showing word as currently guessed, letters left to guess, and lives left
                display_word = "".join(self.word_guessed)
                print(f"Word: {display_word}, Letters to Guess: {self.num_letters}, Lives Left: {self.num_lives}")
                
                # Take user input and set it to lower case
                guess = input("Please guess a letter: ")
                guess = guess.lower()
                
                # Check if the guess is alphabetic and a single character
                # If it isn't then print a message
                if not(guess.isalpha() and len(guess)==1):
                    print("Invalid input. Please enter a single, alphabetic character.")
                
                # If guess has already been used then print a message
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                
                # Othwerise, add the guess onto the list of guesses and call check_guess
                else:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)

h = Hangman(["apple", "banana", "cherry", "peach", "grape", "mango", "pineapple"])
h.ask_for_input()



