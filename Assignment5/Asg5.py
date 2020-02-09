# Joshua Arulsamy
# Assignment 5
# 02/08/2020
# COSC 2049 500
import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
cards = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

# Generate random values
face_val = random.randint(1, 13)
suit_val = random.randint(1, 4)
# Subtract suit by one since list indicies start at zero.
suit_val -= 1

if face_val > 1 and face_val < 11:
    print(f"{face_val} of {suits[suit_val]}")
else:
    print(f"{cards[face_val]} of {suits[suit_val]}")
