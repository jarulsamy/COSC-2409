# Joshua Arulsamy
# Assignment 14
# 04/29/2020
# COSC 2049 500
#

INCORRECT_NUMBER = "\t Incorrect number of items\n"
INVALID_ITEM = "\tInvalid item\n"

with open("payData.txt", "r") as f:
    lines = f.readlines()

out_file = open("payroll.txt", "w")

for i in lines:
    try:
        first, last, hours, rate = i.split()
    except ValueError:
        out_file.writelines([i, INCORRECT_NUMBER])
        continue

    try:
        hours = float(hours)
        rate = float(rate)
    except Exception:
        out_file.writelines([i, INCORRECT_NUMBER])
        continue

    if hours <= 40:
        overtime_hours = 0
        pay = hours * rate
    else:
        overtime_hours = hours - 40
        pay = (40 * rate) + (overtime_hours * rate * 1.5)

    output_1 = f"{first} {last} {hours:.2f} {rate:.2f}\n"
    output_2 = (
        f"\tPay for {first} {last}: ${pay:.2f} (Overtime hours: {overtime_hours:.2f})\n"
    )
    out_file.writelines([output_1, output_2])

out_file.close()
