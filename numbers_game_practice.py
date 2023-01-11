# This is a guess the numbers game.

# imported fx
import random

secretnumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# Asking the player to guess 6 times.
for guessestaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretnumber:
        print("Guess is too low")
    elif guess > secretnumber:
        print("Guess is too high.")
    else:
        break  # correct guess.

if guess == secretnumber:
    print("Good job! You guessed my number in " + str(int(guessestaken)) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretnumber))
