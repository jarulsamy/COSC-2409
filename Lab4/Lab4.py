# Joshua Arulsamy
# Lab 4
# 02/02/2020
# COSC 2049 500

num_cars = float(input("Please input the number of cars you sold this month: "))

if not num_cars.is_integer():
    print("You can't sell part of a car!")
    exit(-1)
if num_cars >= 15:
    commission = num_cars * 500
else:
    commission = num_cars * 300

# Round to 2 decimals.
commission = round(commission, 2)
# Pad the zeros to look nice.
commission = format(commission, ".2f")
print(f"Your commision is ${commission}.")
