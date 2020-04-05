# Joshua Arulsamy
# Assignment 10
# 04/04/2020
# COSC 2049 500
#
# Demonstrates random numbers and elif statements
#
# generates 2 random numbers (rank and suit) for a card
#
# outputs the card
#
# input: none
# process int rank and suit (random numbers between 1 and 3, and 1-4)
# output d1, d2, total
#
# summary data to include count and total
#
# key calculations:
# rank = random.randint(1,13)
# suit = random.randint(1,4)
# test data: no input, but run enough to be sure
#
# include two string returning functions, and 1 int returning function
# for the face, suit, and value
#
# Instructions: The code below does not need any modification except that
# the two functions getFace() and getValue() have not been
# written yet. Notice how getSuit() is written. Write these 2 functions
# where indicated.

import random
random.seed()

# put getFace() here. It is sent the face value (1 to 13), and returns a string
# indicating which card it is. You can use A, K, Q, and J for ace, king, queen, jack, if you wish
#
"""
getFace(r)

This should return a string with the card face. the parameter r will be a value between 1 and 13. The function should return a string such as "King of " or "7 of "

getSuit(s)

Similar to getFace(r) but returns a string with the suit. This is already written for you. Use this as a guide to write the other two

getValue(r)

This should return an int. 10 for face cards, 1 for Ace, the actual number for all others. The parameter r is a number between 1 and 13
"""


def getFace(r):
    cards = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    if r in cards.keys():
        return f"{cards[r]} of "
    else:
        return f"{r} of "


# getSuit(). This function is sent a suit number (1 - 4), and returns a string
# which is the suit.
def getSuit(s):
    if s == 1:
        return "\u2663"
    elif s == 2:
        return "\u2662"
    elif s == 3:
        return "\u2661"
    else:
        return "\u2660"


# put getValue() here. It is sent the face value (1 to 13), and returns an int
# indicating what value the card has. Face cards are 10, aces 1, and all others
# their number (2-10)
def getValue(s):
    values = {"Ace": 1, "Jack": 10, "Queen": 10, "King": 10}
    if s in values.keys():
        return values[s]
    else:
        return s


# here is the actual program. DO NOT MODIFY, DELETE, or ADD anything below here
choice = 1
count = 0
total = 0

while choice == 1:
    rank = random.randint(1, 13)
    suit = random.randint(1, 4)

    # calls to both getFace() and getSuit()
    print("You cut the: " + getFace(rank) + getSuit(suit))

    # call to getValue()
    print("The value of your card is: " + str(getValue(rank)))

    print("Pick another? 1 for yes, 0 for no: ", end='')
    choice = int(input())
    count = count + 1
    total = total + getValue(rank)  # another call to getValue()

print("You picked " + str(count) + " cards for a total of " + str(total))
