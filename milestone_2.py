# My first AICore project - Hangman
import random

# Make a list to contain the possible words
word_list = ["Apple", "Banana", "Mango", "Cherry", "Peach"]
print(word_list)

# Choose a random word from the list of possible words
word = random.choice(word_list)
print(word)

# Get the user's guess using the input command
guess = input("Please enter a letter: ")

# Verify that the user's guess is a single character
# By checking it is of length 1 and is alphabetical

if len(guess)==1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")