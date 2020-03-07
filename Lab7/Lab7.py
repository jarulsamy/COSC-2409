# Joshua Arulsamy
# Lab 7
# 03/06/2020
# COSC 2049 500
import random

# Unicode characters did not work on windows in CMD.
# They worked fine in a linux KDE Konsole session.

# Unicode representation of dice
one = "\u2680"
two = "\u2681"
three = "\u2682"
four = "\u2683"
five = "\u2684"
six = "\u2685"
ucodes = [one, two, three, four, five, six]

# Count wins/losses/points
WINS = 0
LOSSES = 0
POINTS = 0

# Keep going until the user says no.
# Anything other than N/n assumes yes.
while input("Roll? [Y/N] ").lower() != "n":
    # Roll the two dice
    # Between 1 and 6 so point math is easy
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_sum = roll1 + roll2

    # Win conditions
    if roll_sum == 7 or roll_sum == 11:
        WINS += 1
        output_str = "Win"
    # Loss conditions
    elif roll_sum == 2 or roll_sum == 3 or roll_sum == 12:
        LOSSES += 1
        output_str = "Loss"
    # Everything else is just a point
    else:
        POINTS += 1
        output_str = "Point"

    # Show the dice
    # Subtract one so index doesn't exceed 5
    print(f"\n\t{ucodes[roll1-1]} {ucodes[roll2-1]}")
    print(f"\tTotal: {roll_sum}, {output_str}")


print(f"WINS: {WINS}")
print(f"LOSSES: {LOSSES}")
print(f"POINTS: {POINTS}")
