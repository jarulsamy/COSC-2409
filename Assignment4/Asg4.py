# Joshua Arulsamy
# Assignment 4
# 02/02/2020
# COSC 2049 500

hours_worked = float(input("Enter the number of hours you worked: "))
rate = float(input("Enter your hourly rate: "))

# Normal hours
if hours_worked <= 40:
    pay = hours_worked * rate
# Overtime hours
else:
    overtime_hours = hours_worked - 40
    pay = (40 * rate) + (overtime_hours * rate * 1.5)
    print(f"You worked {overtime_hours} overtime hours.")

# Round to 2 decimals
pay = round(pay, 2)
# Pad the zeros to look nice.
pay = format(pay, ".2f")
print(f"You earned ${pay}")
