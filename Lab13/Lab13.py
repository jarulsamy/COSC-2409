# Joshua Arulsamy
# Lab 13
# 04/23/2020
# COSC 2049 500
#
# Auto close on going out of scope.
# Read input data
with open("ctemps.txt", "r") as infile:
    lines = infile.readlines()

# Write to output file.
with open("ftemps2.txt", "w") as outfile:
    for i in lines:
        f = float(i) * (9.0 / 5.0) + 32
        outfile.write(str(f) + "\n")

"""
# Input -> ctemps.txt:

0
32
100

# Output -> ftemps2.txt:

32.0
89.6
212.0
"""
