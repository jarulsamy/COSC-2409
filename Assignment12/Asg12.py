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
    if num > 10 or num == 1:
        num = CARDS[num]

    return suite, num


def print_list(l: list):
    """
    Prints every item in a given list on one line.
    """
    for i in l:
        print(i, end=" ")
    print()


def print_list_len(l: list):
    """
    Prints length of a given list.
    """
    print(f"Length of list: {len(list)}.")


def print_hand(cards: list, values: list):
    """
    Pretty way to print both cards and values together.
    """
    for i, j in zip(cards, values):
        print(f"\t{i} {j}")


while not done:
    while add_cards:
        card, num = random_card()
        print(f"You drew a {num} {card}")
        cards.append(card)
        values.append(num)

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
