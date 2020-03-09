# diceLoopVer2.py
# by Robert Van Cleave
# demonstrates random numbers and if statements
#
# generates 1 random numberbetween 1 and 6,
# then outputs it and the running total
#
# Builds a string of unicode caharacters as we go.
#
#
# input: none
# process int d (random number between 1 and 6)
#
# output string rolls (accumulation of all rolls in unicode),int total
#
# key calculations:
# d = random.randint(1,6)
#
#   use while loop to let the user continue, and build total
#
# test data: no input, but run enough to be sure
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
choice = 1
count = 0
total = 0
rolls = ""
while choice == 1:
    d = random.randint(1, 6)
    total += d
    # print d1 in unicode
    if d == 1:
        rolls += " " + one
    elif d == 2:
        rolls += " " + two
    elif d == 3:
        rolls += " " + three
    elif d == 4:
        rolls += " " + four
    elif d == 5:
        rolls += " " + five
    else:
        rolls += " " + six

    print("So far, you have rolled : " + rolls + " for a total of: " + str(total))

    count += 1  # counter just add one each time
    print("Roll again? 1 for yes, 0 for no: ", end="")
    choice = int(input())

avg = total / count  # averages are calulated after the loop
print(
    "You rolled "
    + str(count)
    + " times with a total of "
    + str(total)
    + " and an average of "
    + str(avg)
)
