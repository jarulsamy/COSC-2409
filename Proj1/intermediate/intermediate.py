# Joshua Arulsamy
# Project 1 - Intermidiate
# 03/25/2020
# COSC 2049 500

# Totals to keep track of
# Each is list, pos correlated with plan.
num_customers = [0, 0, 0]
total_data = [0, 0, 0]
total_taxes = [0, 0, 0]
total_all_bills = [0, 0, 0]
done = False

rates = [24.99, 39.99, 54.99]
free_data = [0, 1, 3]
while not done:
    # Prompt the user for data
    name = input("Enter your name: ")
    plan = int(input("Select a plan (1, 2, or 3): "))
    data = int(input("Enter data usage (int): "))
    int_plan = input("Do you have an international calling plan [Y/N]: ")
    int_min = int(input("Enter international minutes: "))

    # Convert int_plan str input to bool
    if int_plan.lower() == "y":
        int_plan = True
    else:
        int_plan = False

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

    # Internation plan
    if int_plan:
        int_plan_charge = 20
        if int_min > 100:
            int_charge = ((int_min - 100) * 0.10)
        else:
            int_charge = 0
    else:
        int_plan_charge = 0
        int_charge = int_min

    # Calculate the rest of the stats
    sub_total = sum([rate_charge, data_charge, int_plan_charge, int_charge])
    tax = sub_total * 0.06
    total = sub_total + tax

    # Update the totals
    num_customers[plan - 1] += 1
    total_data[plan - 1] += data
    total_taxes[plan - 1] += tax
    total_all_bills[plan - 1] += total

    # Display the per customer stats
    print(f"\n\t{name}:")
    print(f"\t${format(rates[plan-1], '.2f')} (Plan: {plan})", end="")
    print(" - Base Rate Charge")

    print(f"\t${format(data_charge, '.2f')} ({format(data, '.2f')}", end="")
    print(f"GB, ${free_data[plan-1]} GB Free) - Data Charge")

    print(f"\t{format(int_plan_charge, '.2f')} ({'Yes' if int_plan else 'No'}) - International Plan")
    print(f"\t${format(int_charge, '.2f')} ({int_min} min.) - International Minutes")

    print(f"\t${format(tax, '.2f')} - 6% Tax")
    print(f"\t${format(total, '.2f')} - Total")

    # Stop/Continue Loop
    loop = input("\nAdd another customer? [Y/N]: ")
    if loop.lower() == "n":
        done = True


# Display the totals by plan
for i in range(3):
    print(f"\nPlan {i+1}")
    print(f"\n\t{num_customers[i]} Customer(s).")
    print(f"\t{format(total_data[i], '.2f')} GB downloaded.")
    print(f"\t${format(total_taxes[i], '.2f')} taxes collected.")
    print(f"\t${format(total_all_bills[i], '.2f')} total of all bills.")
    if num_customers[i] == 0:
        print(f"\tN/A average bill.")
    else:
        print(f"\t${format(total_all_bills[i]/num_customers[i], '.2f')} average bill.")
