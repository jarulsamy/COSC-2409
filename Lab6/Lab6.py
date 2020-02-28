# Joshua Arulsamy
# Lab 6
# 02/28/2020
# COSC 2049 500

hours_worked = 1
num_employees = 0
total_gross_pay = 0

while hours_worked > 0:
    hours_worked = float(input("Enter the number of hours you worked (-1 to quit): "))

    if hours_worked < 0:
        break

    rate = float(input("Enter your hourly rate (-1 to quit): "))

    if rate < 0:
        break

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

    # Increment the counters
    num_employees += 1
    total_gross_pay += pay

    # Pad the zeros and print.
    pay = format(pay, ".2f")
    print(f"You earned ${pay}")


print(f"Total number of employees {num_employees}")
print(f"Total gross pay: ${total_gross_pay}")
print(f"Average gross pay: ${round(total_gross_pay / num_employees, 2)}")
