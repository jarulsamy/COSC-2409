# Joshua Arulsamy
# Lab 11
# 04/10/2020
# COSC 2049 500

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

done = False

while not done:
    user_input = -1

    # Keep asking the user for an input if it's invalid.
    while user_input > 12 or user_input < 1:
        user_input = int(input("Enter a number between 1 and 12: "))

    # Show the corresponding month.
    print(f"Month {user_input} is {months[user_input - 1]}")

    # Should loop again?
    done_ = input("Continue [Y/N]: ")
    if done_.lower() != "y":
        done = True

# Sample Output
"""
Enter a number between 1 and 12: 1
Month 1 is January
Continue [Y/N]: y
Enter a number between 1 and 12: 2
Month 2 is February
Continue [Y/N]: y
Enter a number between 1 and 12: 3
Month 3 is March
Continue [Y/N]: y
Enter a number between 1 and 12: 4
Month 4 is April
Continue [Y/N]: y
Enter a number between 1 and 12: 5
Month 5 is May
Continue [Y/N]: y
Enter a number between 1 and 12: 6
Month 6 is June
Continue [Y/N]: y
Enter a number between 1 and 12: 7
Month 7 is July
Continue [Y/N]: y
Enter a number between 1 and 12: 8
Month 8 is August
Continue [Y/N]: y
Enter a number between 1 and 12: 9
Month 9 is September
Continue [Y/N]: y
Enter a number between 1 and 12: 10
Month 10 is October
Continue [Y/N]: y
Enter a number between 1 and 12: 11
Month 11 is November
Continue [Y/N]: y
Enter a number between 1 and 12: 12
Month 12 is December
Continue [Y/N]: n
"""
