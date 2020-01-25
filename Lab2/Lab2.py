# Joshua Arulsamy
# Lab 2
# 1/24/2020
# COSC 2049 500


currency_input = float(input("Enter some currency amount: "))
dollars = int(currency_input)
cents = int((currency_input - dollars) * 100 + 0.49)

print(f"${currency_input} is {dollars} Dollars and {cents} Cents.")
