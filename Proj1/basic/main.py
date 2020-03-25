# Joshua Arulsamy
# Project 1 - Basic
# 03/24/2020
# COSC 2049 500

# Totals to keep track of
num_customers = 0
total_data = 0
total_taxes = 0
total_all_bills = 0
done = False

rates = [24.99, 39.99, 54.99]
free_data = [0, 1, 3]
while not done:
    # Prompt the user for data
    name = input("Enter your name: ")
    plan = int(input("Select a plan (1, 2, or 3): "))
    data = int(input("Enter data usage (int): "))

    # Select the plan
    # Calculate based on corresponding rates
    if plan == 1:
        rate_charge = rates[0]
        data_charge = 15 * data
    elif plan == 2:
        rate_charge = rates[1]
        if data > 1:
            data_charge = (data - 1) * 10
        else:
            data_charge = 0
    elif plan == 3:
        rate_charge = rates[2]
        if data > 3:
            data_charge = (data - 3) * 7.5
        else:
            data_charge = 0

    # Calculate the rest of the stats
    sub_total = rate_charge + data_charge
    tax = sub_total * 0.06
    total = sub_total + tax

    # Update the totals
    num_customers += 1
    total_data += data
    total_taxes += tax
    total_all_bills += total

    # Display the stats
    print(f"\n\t{name}:")
    print(f"\t${format(rates[plan-1], '.2f')} (Plan: {plan})", end="")
    print(" - Base Rate Charge")

    # print(f"\t{format(data, '.2f')} GB: ${data_charge} - Data Charge")
    print(f"\t${format(data_charge, '.2f')} ({format(data, '.2f')}", end="")
    print(f"GB, ${free_data[plan-1]} GB Free.) - Data Charge")

    print(f"\t${format(tax, '.2f')} - Tax")
    print(f"\t${format(total, '.2f')} - Total")

    # Stop/Continue Loop
    loop = input("\nAdd another customer? [Y/N]: ")
    if loop.lower() == "n":
        done = True

# Display the totals
print(f"\n\tTotal number of customers: {format(num_customers)}.")
print(f"\tTotal data downloaded: {format(total_data, '.2f')} GB.")
print(f"\tTotal taxes collected: ${format(total_taxes, '.2f')}.")
print(f"\tTotal of all bills ${format(total_all_bills, '.2f')}.")
