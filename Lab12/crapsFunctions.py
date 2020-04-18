# crapsFunctions.py
#
# by Robert Van Cleave
#
# Plays a simple game of craps:
#       roll a pair of dice, and detrmine outcome as follows:
#           7 or 11: "You win"
#           2, 3 or 12: "You lose"
#           all others:
#               the roll is now called the point.
#               loop until the user rolls the point (win) or
#                   a 7 (lose)
#
# allow user to repeat as they wish. Keep track of wins, loses
#
#   input: 1 or 0 to continue
#   process: none
#   output: detail: the two dice (unicode) and the total, message as above
#           summary: count of wins, loses, and points
#
# key calculations and logic:
# use while loop and an int loop control variable for main loop
# use another loop (nested) for point round
#
# Function:
#   rollDice()
#       parameters: none
#       output: two die (randomly determined)
#       return: the total of the dice (int)
#
#   test data: run enough times to be sure all is in order
#
import random

random.seed()

one = "\u2680"
two = "\u2681"
three = "\u2682"
four = "\u2683"
five = "\u2684"
six = "\u2685"


def rollDice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    print("You rolled : ", end="")
    # print d1 in unicode
    if d1 == 1:
        print(one + " ", end="")
    elif d1 == 2:
        print(two + " ", end="")
    elif d1 == 3:
        print(three + " ", end="")
    elif d1 == 4:
        print(four + " ", end="")
    elif d1 == 5:
        print(five + " ", end="")
    else:
        print(six + " ", end="")

    # print d2 in unicode
    if d2 == 1:
        print(one + " ", end="")
    elif d2 == 2:
        print(two + " ", end="")
    elif d2 == 3:
        print(three + " ", end="")
    elif d2 == 4:
        print(four + " ", end="")
    elif d2 == 5:
        print(five + " ", end="")
    else:
        print(six + " ", end="")

    print("for a total of " + str(total))

    return total
    # end of function


wins = 0
losses = 0
choice = 1
while choice == 1:
    roll = rollDice()
    if roll == 7 or roll == 11:
        print(" You win!")
        wins += 1
    elif roll == 2 or roll == 3 or roll == 12:
        print(" You lose!")
        losses += 1
    else:
        point = roll
        print(" You rolled a point: " + str(point))
        done = False
        while not done:
            # this type of statement is sometimes called a "pause"
            input("Hit enter to roll....")
            roll = rollDice()
            if roll == point:
                done = True
                print("You win!")
                wins += 1
            elif roll == 7:
                done = True
                print("You lose")
                losses += 1
    print("Play again? 1 for yes, 0 for no: ", end="")
    choice = int(input())

print("Final results:\n\tWins: " + str(wins) + "\n\tLoses: " + str(losses))
