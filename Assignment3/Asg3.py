# Joshua Arulsamy
# Assignment 3
# 02/02/2020
# COSC 2049 500

import math

inputs = {
    "X1": None,
    "Y1": None,
    "X2": None,
    "Y2": None
}

for i in inputs:
    inputs[i] = float(input(f"Please enter {i}: "))

distance = (inputs["Y2"] - inputs["Y1"]) ** 2 + (inputs["X2"] - inputs["X1"]) ** 2
distance = math.sqrt(distance)
print(f"The distance is {round(distance, 2)}")
