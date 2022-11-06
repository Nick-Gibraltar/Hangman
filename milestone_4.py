# AICore Project 1 - Hangman
import random

class Hangman:

        def __init__(self, word_list, num_lives=5):

            self.word_list = word_list
            self.num_lives = num_lives
            self.word = random.choice(word_list)
            self.word_guessed = len(self.word) * ["_"]
            self.num_letters = 0
            self.list_of_guesses = []
        
        

