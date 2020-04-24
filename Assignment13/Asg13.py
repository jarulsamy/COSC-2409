# Joshua Arulsamy
# Assignment 13
# 04/23/2020
# COSC 2049 500

POUNDS_FILE = "pounds.txt"
NEWTONS_FILE = "newtons.txt"
KILOS_FILE = "kilos.txt"

with open(POUNDS_FILE, "r") as infile:
    pounds = infile.readlines()

newtons_file = open(NEWTONS_FILE, "w")
kilos_file = open(KILOS_FILE, "w")

for i in pounds:
    p = float(i)

    # One lb is approximately 4.45 N.
    newtons = p * 4.45
    kilos = p / 2.2046

    newtons_file.write(str(newtons) + "\n")
    kilos_file.write(str(kilos) + "\n")


newtons_file.close()
kilos_file.close()

"""
# pounds.txt

1.0
2.0
3.0
4.0
5.0
10.0
15.0
250.0
123.123
5984.1023
12312.34534
"""

"""
# newtons.txt

4.45
8.9
13.350000000000001
17.8
22.25
44.5
66.75
1112.5
547.8973500000001
26629.255235
54789.936763000005
"""

"""
# kilos.txt

0.4535970244035199
0.9071940488070398
1.3607910732105597
1.8143880976140796
2.2679851220175995
4.535970244035199
6.803955366052798
113.39925610087997
55.84822643563458
2714.370997006259
5584.843209652544
"""
