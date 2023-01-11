# Rock, Paper, Scissors Game

# imported modules
import random, sys

print("Rock, Paper, Scissors")

# score variables
wins = 0
losses = 0
ties = 0

# Main game loop
while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))

    # Player input loop
    while True:
        print("Enter your move: (r) Rock (p) Paper (s) Scissors or (q) Quit")
        playermove = input()
        if playermove == "q":
            sys.exit
        if playermove == "r" or playermove == "p" or playermove == "s":
            break
        print("Type one of r, p, s, or q.")
    # Display what the player chooses.
    if playermove == "r":
        print("Rock vs... ")
    elif playermove == "s":
        print("Scissors vs... ")
    elif playermove == "p":
        print("Scissors vs... ")
    # Display what the Computer chooses.
    randomnumber = random.randint(1, 3)
    if randomnumber == 1:
        computermove = "r"
        print("Rock")
    elif randomnumber == 2:
        computermove = "s"
        print("Scissors")
    elif randomnumber == 3:
        computermove = "p"
        print("Paper")
    # Display and record the win/loss/ties
    if playermove == computermove:
        print("Tied")
        ties = ties + 1
    elif playermove == "r" and computermove == "s":
        print("You win!")
        wins = wins + 1
    elif playermove == "p" and computermove == "r":
        print("You win!")
        wins = wins + 1
    elif playermove == "s" and computermove == "p":
        print("You win!")
        wins = wins + 1
    elif playermove == "r" and computermove == "p":
        print("You lose!")
        losses = losses + 1
    elif playermove == "p" and computermove == "s":
        print("You lose!")
        losses = losses + 1
    elif playermove == "s" and computermove == "r":
        print("You lose!")
        losses = losses + 1
    print("Do you want to play again? (y/n)")
    play_again = input()
    if play_again == "n":
        break
