# Joshua Arulsamy
# Assignment 7
# 03/09/2020
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


def roll():
    # Roll the two dice
    # Between 1 and 6 so point math is easy
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_sum = roll1 + roll2
    return roll_sum, f"{ucodes[roll1 - 1]} {ucodes[roll2 - 1]}"


# Keep going until the user says no.
# Anything other than N/n assumes yes.
while input("Roll? [Y/N] ").lower() != "n":
    roll_sum, ucode_dice = roll()

    # Win conditions
    if roll_sum == 7 or roll_sum == 11:
        WINS += 1
        print(f"\t{ucode_dice}: {roll_sum} Win")
    # Loss conditions
    elif roll_sum == 2 or roll_sum == 3 or roll_sum == 12:
        LOSSES += 1
        output_str = "Loss"
        print(f"\t{ucode_dice}: {roll_sum} Loss")
    # Everything else is just a point
    else:
        done = False
        # Reroll until 7 (loss) or their original roll (win).
        while not done:
            new_sum, ucode_dice = roll()
            if new_sum == 7:
                done = True
                LOSSES += 1
                print(f"\t{ucode_dice}: {new_sum} Loss")
            elif new_sum == roll_sum:
                done = True
                WINS += 1
                print(f"\t{ucode_dice}: {new_sum} Win")
            # Show the number of rerolls (debug)
            # else:
            #     print(".", end="")

# Show total wins/losses
print(f"WINS: {WINS}")
print(f"LOSSES: {LOSSES}")
