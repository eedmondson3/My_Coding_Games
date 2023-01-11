# imports
import random


# Player input loop
while True:
    print("Ask your question, mortal.")
    playermove = input()

    def getAnswer(answerNumber):
        if answerNumber == 1:
            return "It is certain"
        elif answerNumber == 2:
            return "It is decidely so"
        elif answerNumber == 3:
            return "Yes"
        elif answerNumber == 4:
            return "Reply is hazy, try again"
        elif answerNumber == 5:
            return "Ask again later"
        elif answerNumber == 6:
            return "Concentrate and ask again"
        elif answerNumber == 7:
            return "My reply is no"
        elif answerNumber == 8:
            return "Outlook is not good"
        elif answerNumber == 9:
            return "Very doubtful"

    print(getAnswer(random.randint(1, 9)))
    print("Do you want to play again? (y/n)")
    play_again = input()
    if play_again == "n":
        break
