# AICore Project 1 - Hangman
import random

class Hangman:

        def __init__(self, word_list, num_lives=5):

            self.word_list = word_list                      # List containing the possible words
            self.num_lives = num_lives                      # Number of lives
            self.word = random.choice(word_list)            # The actual word to be guessed chosen from word_list
            self.num_letters = len(self.word)               # Number of letters in the word
            self.list_of_guesses = []                       # List to store the letters already guessed
            self.word_guessed = self.num_letters * ["_"]    # Represents the partially guessed word        


        def check_guess(self, guess):

            if guess in self.word:                          # If the target word contains the guessed letter
                print(f"Good guess! {guess} is in the word.")
                for i, j in enumerate(self.word):           # Iterate through the target word 
                    if guess==j:                            # And set the elements of word_guessed to be equal
                        self.word_guessed[i]=j              # to the guessed letter in the appropriate place
                        self.num_letters -=1
            else:
                self.num_lives -=1                          # If it's not, then lose a life and print a message
                print(f"Sorry, {guess} is not in the word.")


        def ask_for_input(self):

            display_word = "".join(self.word_guessed)       # Print a message showing game_status
            print(f"\nWord: {display_word}, Letters to Guess: {self.num_letters}, Lives Left: {self.num_lives}\n")
            
            guess = input("Please guess a letter: ")        # Take user input
            guess = guess.lower()                           # Set it to lower case
            
            if not(guess.isalpha() and len(guess)==1):      # Check if gusess is alphabetic and a single character
                print("Invalid input. Please enter a single, alphabetic character.")    # If it isn't, print a character
            
            elif guess in self.list_of_guesses:             # If guess has already been used
                print("You already tried that letter!")     # Then print a message
            
            else:                                           # Otherwise,
                self.list_of_guesses.append(guess)          # Add the guess onto the list of guesses
                self.check_guess(guess)                     # And call check_guess

def play_game(word_list, num_lives):

    game = Hangman(word_list, num_lives)                    # Make game an instance of the Hangman class
    game_over = False                                       # game_over indicates whether the game is over
 
    while not game_over:                                    # Loop so long as not game_over
        game.ask_for_input()                                # Call ask_for_input method

        if game.num_letters==0:                             # If num_letters reaches zero then word has been guessed
            print("Well done! You found the word.")         # Print a message
            game_over = True                                # And set game_over to be True
 
        elif game.num_lives==0:                             # If num_lives reaches zero then player has run out of lives
            print("Oh dear! You ran out of lives.")         # Print a message
            game_over = True                                # Set game_over to be True

play_game(["commode","harbinger","transport","tumultuous","benign","variable"],10)