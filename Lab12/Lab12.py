# Joshua Arulsamy
# Lab 11
# 04/10/2020
# COSC 2049 500
import random

random.seed()


def die():
    d = random.randint(1, 6)
    if d == 1:
        face = "\u2680"
        num = 1
    elif d == 2:
        face = "\u2681"
        num = 2
    elif d == 3:
        face = "\u2682"
        num = 3
    elif d == 4:
        face = "\u2683"
        num = 4
    elif d == 5:
        face = "\u2684"
        num = 5
    else:
        face = "\u2685"
        num = 6

    return face, num


def dice():
    d1, value1 = die()
    d2, value2 = die()
    return d1 + " " + d2, value1 + value2


# Count wins/losses/points
WINS = 0
LOSSES = 0
POINTS = 0

# Keep going until the user says no.
# Anything other than N/n assumes yes.
while input("Roll? [Y/N] ").lower() != "n":

    faces, value = dice()

    # Win conditions
    if value == 7 or value == 11:
        WINS += 1
        output_str = "Win"
    # Loss conditions
    elif value == 2 or value == 3 or value == 12:
        LOSSES += 1
        output_str = "Loss"
    # Everything else is just a point
    else:
        POINTS += 1
        output_str = "Point"

    # Show the dice
    # Subtract one so index doesn't exceed 5
    print(f"\n\t{faces}")
    print(f"\tTotal: {value}, {output_str}")


print(f"WINS: {WINS}")
print(f"LOSSES: {LOSSES}")
print(f"POINTS: {POINTS}")
