# Joshua Arulsamy
# Assignment 11
# 04/13/2020
# COSC 2049 500
import random

# Unicode symbols for suites
SUITE = ["\u2663", "\u2662", "\u2661", "\u2660"]
# Num to proper name
CARDS = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
# Initialize user hand
hand = []

done = False
add_cards = True


def random_card():
    """
    Chooses a random card from deck
    """
    suite = random.choice(SUITE)
    num = random.randint(1, 13)
    if num > 10 or num == 1:
        num = CARDS[num]

    return f"{num} {suite}"


def print_list(l: list):
    """
    Prints every item in a list.
    """
    for i in l:
        print(i)


while not done:
    while add_cards:
        card = random_card()
        print(f"You drew a {card}")
        hand.append(card)

        resp = input("Draw again? [Y/n]: ")
        if resp.lower() == "n":
            add_cards = False

    resp = input("0 for restart, 1 to quit: ")
    if resp == "0":
        hand = []
        add_cards = True
    elif resp == "1":
        done = True
        print("Your hand:")
        print_list(hand)
