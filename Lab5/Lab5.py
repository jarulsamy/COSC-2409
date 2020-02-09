# Joshua Arulsamy
# Lab 5
# 02/08/2020
# COSC 2049 500
import random

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)

print(f"You rolled a {num1} and a {num2} for a total of {num1 + num2}.")

if num1 == num2:
    print("Doubles!")
