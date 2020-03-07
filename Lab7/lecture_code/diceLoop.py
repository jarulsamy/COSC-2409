# diceLoop.py
# by Robert Van Cleave
# demonstrates random numbers and if statements
#
# generates 2 random numbers (rolls) between 1 and 6, then outputs them and the total
# output "doubles" if the rolls are the same
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
#   use while loop to let the user continue
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

while choice == 1:
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
        print("Doubles!")

    count = count + 1
    # counter just add one each time
    total = total + roll  # accumulators add up some value
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
