# Joshua Arulsamy
# Assignment 2
# 1/24/2020
# COSC 2049 500

currency_input = float(input("Enter some currency amount: "))
dollars = int(currency_input)
cents = int((currency_input - dollars) * 100 + 0.49)

bill_map = {
    "One hundred": 100,
    "Fifty": 50,
    "Twenty": 20,
    "Ten": 10,
    "Five": 5,
    "One": 1,
}

coin_map = {
    "Quarters": 25,
    "Dimes": 10,
    "Nickels": 5,
    "Pennies": 1
}

# Calculate bills
remainder = dollars
for k, v, in bill_map.items():
    print(f"{k} dollar bills: {remainder // v}")
    remainder %= v

# Calculate coins
remainder = cents
for k, v in coin_map.items():
    print(f"{k}: {remainder // v}")
    remainder %= v
