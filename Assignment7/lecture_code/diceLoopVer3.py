# diceLoopMisc.py
# by Robert Van Cleave
# demonstrates misc stuff
#
# generates 2 random numbers (rolls) between 1 and 6, then outputs them and the total
# output "doubles" if the rolls are the same
#
#  will continue to roll until a 7 or 11 is rolled
#
#  Uses unicode characters to display the individual dice
#
# input: none
# process int d1, d2 (random numbers between 1 and 6)
# output d1, d2, total
#
# key calculations:
# d1 (and d2) = random.randint(1,6)
#
#   use while loop to roll until done
#
# test data: no input, but run enough to be sure
#   summary data: #of rolls above and below 7
#
import random

random.seed()
# the above two lines must be there to work right

one = "\u2680"
two = "\u2681"
three = "\u2682"
four = "\u2683"
five = "\u2684"
six = "\u2685"

high = 0
low = 0
count = 0
roll = 0  # just to start things off
doubles = False
print("Rolling until a 7 or 11, or doubles")
while (roll != 7 and roll != 11) and not doubles:
    input(
        "Hit enter to roll...."
    )  # this type of statement is sometimes called a "pause"
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    roll = d1 + d2
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

    print(" for a total of " + str(roll))
    if d1 == d2:
        doubles = True
        print("Doubles!")

    if roll > 7:
        high += 1  # shortcut for: high = high + 1
    elif roll < 7:
        low += 1

    count += 1


print(
    "You rolled "
    + str(count)
    + " times, with\n\t"
    + str(high)
    + " over 7 and\n\t"
    + str(low)
    + " under"
)
