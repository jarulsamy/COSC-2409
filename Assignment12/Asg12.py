# Joshua Arulsamy
# Assignment 12
# 04/20/2020
# COSC 2049 500
import random

# Unicode symbols for suites
SUITE = ["\u2663", "\u2662", "\u2661", "\u2660"]
# Num to proper name
CARDS = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
# Two lists to track user hand.
cards = []
values = []

done = False
add_cards = True


def random_card():
    """
    Chooses a random card from deck
    """
    suite = random.choice(SUITE)
    num = random.randint(1, 13)

    return suite, num


def print_list(l: list):
    """
    Prints every item in a given list on one line.
    """
    for i in l:
        print(i, end=" ")
    print()


def total(l: list):
    """
    Prints length of a given list.
    """
    total = 0

    for i in l:
        total += i

    return total


def print_hand(cards: list, values: list):
    """
    Pretty way to print both cards and values together.
    """
    for i, j in zip(cards, values):
        print(f"\t{i} {j}")


while not done:
    while add_cards:
        card, num = random_card()
        cards.append(card)
        values.append(num)

        if num > 10 or num == 1:
            num = CARDS[num]
        print(f"You drew a {num} {card}")

        resp = input("Draw again? [Y/n]: ")
        if resp.lower() == "n":
            add_cards = False

    resp = input("0 for restart, 1 to quit: ")
    if resp == "0":
        hand = []
        add_cards = True

    elif resp == "1":
        done = True
        print()
        print("Your hand:")
        print_hand(cards, values)
        print()
        print(f"\tTotal Value: {total(values)}")
