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


choice = 1
while choice == 1:
    bothDice, bothValue = dice()

    print("You rolled: " + bothDice + " = " + str(bothValue))
    print("Enter 1 to roll again, 0 to stop: ", end="")
    choice = int(input())
