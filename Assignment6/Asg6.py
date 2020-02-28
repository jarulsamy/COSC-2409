# Joshua Arulsamy
# Assignment 6
# 02/28/2020
# COSC 2049 500
import random

continue_ = True

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
cards = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
values = {"Ace": 1, "Jack": 10, "Queen": 10, "King": 10}

total_drew = 0
total_value = 0
while continue_:

    # Generate random values
    face_val = random.randint(1, 13)
    suit_val = random.randint(0, 3)

    if face_val > 1 and face_val < 11:
        print(f"{face_val} of {suits[suit_val]}, value: {face_val}")
        total_value += face_val
    else:
        value = values[cards[face_val]]
        print(f"{cards[face_val]} of {suits[suit_val]}, value: {value}")
        total_value += value

    # Keep track of total number drawn
    total_drew += 1

    should_continue = input("Stop drawing? [y/N]: ")
    # Stop if user inputs y, blank input just continues
    if "y" in should_continue.lower():
        continue_ = False

print(f"\n\tYou drew {total_drew} cards.")
print(f"\tTotal value: {total_value}.")
